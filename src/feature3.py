# feature3.py
# Insight Data Engineering Coding Challenge, 2016 November
# Katrina Sitkovits, katrina.sitkovits@gmail.com
#
# This program implements Feature 3 of the coding challenge by
# verifying users up to 4 degrees away in the friends network
#
# Helper functions imported from paymo_functions.py file in ./src/ directory

import sys
from paymo_functions import construct_initial_graph
from paymo_functions import stream_payments

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
stream_payments (graph, stream_payment_file, output_file, max_degree_separation)