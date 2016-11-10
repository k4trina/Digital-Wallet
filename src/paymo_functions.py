# paymo_functions.py
# Insight Data Engineering Coding Challenge, 2016 November
# Katrina Sitkovits, katrina.sitkovits@gmail.com
#
# This file contains helper functions for Features 1, 2, 3, and additional Feature 4
#

# Get sender and receiver IDs from payment line
# ID1 = sender (tx), ID2 = receiver (rx)
def get_IDs ( line ):
    index = 0
    tx = 0
    rx = 0
    for segment in line.split(', '):
        # ignore timestamp (index==0)
        if (index == 1):
            tx = segment
        elif (index == 2):
            rx = segment
            break  # ignore payment amount and user message
        index += 1
    return tx, rx


# Update graph connections based on incoming payment records from stream
# Assume all new connections in the graph are marked valid
def update_graph ( graph, tx, rx ):
    if tx in graph:
        if rx not in graph[tx]: graph[tx].append(rx)
    else:
        graph[tx] = [rx]
    if rx in graph:
        if tx not in graph[rx]: graph[rx].append(tx)
    else:
        graph[rx] = [tx]
    return


# Construct initial network graph of users/friends from batch file
def construct_initial_graph ( graph, batch_payment_file ):
    batch_payment_input = open(batch_payment_file, "r")
    firstline = True
    for line in batch_payment_input:
        if firstline:
            firstline = False
            continue
        tx, rx = get_IDs(line)
        update_graph(graph, tx, rx)
    batch_payment_input.close()


# Depth-first search traverses graph starting from vertex node,
# and visits all children that haven't previously been visited
# Returns trusted if node is found within max number of search degree levels
def dfs (graph, vertex, rx, level, visited, max_search_degree):
    trusted = False
    visited.add(vertex)
    vertex_children = set(graph[vertex])-visited
    if rx in vertex_children:
        trusted = True
    else:
        if level < max_search_degree-1:
            for child in vertex_children:
                trusted = dfs(graph,child,rx,level+1,visited,max_search_degree)
                if trusted: break
    return trusted


# Stream payments from stream file
def stream_payments(graph, stream_payment_file, output_file, max_levels):
    stream_payment_input = open(stream_payment_file, "r")
    output_verified = open(output_file, "w")
    firstline = True
    for line in stream_payment_input:
        if firstline:
            firstline = False
            continue
        tx, rx = get_IDs(line)
        # Perform depth-first search to find receiver up to max_levels of degree separation
        if dfs(graph, tx,rx,0,set(),max_levels): output_verified.write("trusted\n")
        else: output_verified.write("unverified\n")
        # Update network graph since the payment is assumed to be verified once completed
        update_graph(graph,tx,rx)
    stream_payment_input.close()
    output_verified.close()




# RSA-encrypted payment stream from sender to PayMo
# This function implements a more secure version of the stream_payments() function above.
# PayMo first generates both a public and private key using the RSA encryption scheme.
# PayMo shares the public key with all verified users in the graph/network.
# PayMo does not reveal the private key to anyone else.
# When a sender performs a payment, we assume that the payment stream/record
# {timestamp, ID1, ID2, amount, message} is encrypted by the sender using PayMo's public key.
# PayMo decrypts each incoming payment record in the stream using our private key.
# We then verify if the transaction is trusted as in Feature 3.
# This function requires the Python developer package, and the following libraries: crypto and pycrypto
#   $ sudo apt-get install python-dev
#   $ sudo apt install python-pip
#   $ pip install crypto
#   $ pip install pycrypto
from Crypto.PublicKey import RSA
from Crypto import Random
def encrypted_stream_payments(graph, stream_payment_file, output_file, max_levels):

    # RSA preamble -- PayMo side
    key = RSA.generate(2048, Random.new().read)             # create RSA key object
    my_private_key = key.exportKey('PEM')                   # generate PayMo's private key
    paymo_private_RSA_obj = RSA.importKey(my_private_key)   # PayMo's private key object
    my_public_key = key.publickey().exportKey('PEM')        # generate PayMo's public key

    stream_payment_input = open(stream_payment_file, "r")
    output_verified = open(output_file, "w")
    firstline = True
    for line in stream_payment_input:
        if firstline:
            firstline = False
            continue

        # Assume that each senders first encrypts the stream payment string with PayMo public key
        user_public_RSA_obj = RSA.importKey(my_public_key)  # each user creates an RSA object using PayMo's public key
        msg_plaintext = str(line)
        msg_encypted = user_public_RSA_obj.encrypt(msg_plaintext, 0)

        # Assume that the payment/message transmission occurs here

        # PayMo decrypts each incoming stream payment with our own private key
        msg_decrypted = paymo_private_RSA_obj.decrypt(msg_encypted)

        # Perform the same remaining steps on the PayMo side
        tx, rx = get_IDs(msg_decrypted)
        if dfs(graph, tx,rx,0,set(),max_levels): output_verified.write("trusted\n")
        else: output_verified.write("unverified\n")
        update_graph(graph,tx,rx)

    stream_payment_input.close()
    output_verified.close()
