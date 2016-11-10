# feature4.py
# Insight Data Engineering Coding Challenge, 2016 November
# Katrina Sitkovits, katrina.sitkovits@gmail.com
#
# Feature 4 extends Feature 3 by implementing asymmetric security based on RSA between the payment
# sender (ID1) and PayMo. The encrypted_stream_payments() function is a modified version of the
# stream_payments() function used in Features 1, 2, and 3. The function encrypts each payment stream
# record from the sender to PayMo using PayMo's public key. PayMo uses their private key to decrypt
# the payment request before verifying the transaction in the friends network.
#
# Feature 4 requires the Python developer package, and the following libraries: crypto and pycrypto
# They can be installed as follows:
#   $ sudo apt-get install python-dev
#   $ sudo apt install python-pip
#   $ pip install crypto
#   $ pip install pycrypto
#
# Helper functions imported from paymo_functions.py file in ./src/ directory
#

import sys
from paymo_functions import construct_initial_graph
from paymo_functions import encrypted_stream_payments

# Open input and output file streams
batch_payment_file = sys.argv[1];
stream_payment_file = sys.argv[2];
output_file = sys.argv[3];

# Instantiate graph of payment IDs, each ID is a node in the graph
graph = {}

# Construct initial graph of friends network
construct_initial_graph (graph, batch_payment_file)

# Stream payments, and verify users up to 4 degrees away in friends network
max_degree_separation = 4
encrypted_stream_payments (graph, stream_payment_file, output_file, max_degree_separation)