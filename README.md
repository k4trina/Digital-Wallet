# Digital-Wallet

## Developer: Katrina Sitkovits
## Email: katrina.sitkovits@gmail.com
## Date: November 10, 2015

Programming Langugage: Python

The Digital Wallet project implements PayMo verification as part of the Insight Data Engineering coding challenge here:
https://github.com/InsightDataScience/digital-wallet

Features 1, 2, and 3 of the challenge are implemented using a depth-first search through a graph representing the PayMo user network. Feature 4 is an additional feature that extends Feature 3 by implementing asymmetric security based on RSA to encrypt stream payments coming from the sender. Additional details regarding Feature 4 are provided below.

The run.sh script executes each feature project independently. Each feature creates a single output text file based on the batch_payment.txt and stream_payment.txt files provided. Each feature first constructs the initial state of the user network, and then verifies incoming stream payment requests.

Features 1, 2, and 3 only require the standard Python sys library.

Feature 4 requires the Python developer package, and the following libraries: crypto and pycrypto
They can be installed as follows:
$ sudo apt-get install python-dev
$ sudo apt install python-pip
$ pip install crypto
$ pip install pycrypto
