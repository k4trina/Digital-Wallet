# Digital-Wallet

#### Developer: Katrina Sitkovits
#### Email: katrina.sitkovits@gmail.com
#### Date: November 10, 2016
#### Programming Langugage: Python

The Digital Wallet project implements PayMo verification as part of the Insight Data Engineering coding challenge here:
https://github.com/InsightDataScience/digital-wallet

Features 1, 2, and 3 of the challenge are implemented using a depth-first search through a graph representing the PayMo user network. Feature 4 is an additional feature that extends Feature 3 by implementing asymmetric security based on RSA to encrypt stream payments coming from the sender. Additional details regarding Feature 4 are provided below.

The ```run.sh``` script executes each feature project independently. Each feature creates a single output text file based on the batch_payment.txt and stream_payment.txt files provided. Each feature first constructs the initial state of the user network, and then verifies incoming stream payment requests.

Features 1, 2, and 3 only require the standard Python ```sys``` library.


### Extra Feature 4: RSA encryption

Feature 4 requires the Python developer package, and the following libraries: ```crypto``` and ```pycrypto```
They can be installed as follows:
```
$ sudo apt-get install python-dev
$ sudo apt install python-pip
$ pip install crypto
$ pip install pycrypto
```

PayMo generates both a private and public key to enable users to encrypt the payment stream they send to PayMo. PayMo shares the public key with all users on the network, while keeping the private key secret. Users can encrypt their messages using PayMo's public key, however, only PayMo can decrypt the message by using the private key. PayMo generates RSA-2048 keys with 2048 bits for increased security since there is currently no proven implementation for factoring RSA numbers beyond 768 bits. 

The figure below shows the Feature 4 implementation where the sending user first encrypts their payment stream message, and then PayMo decrypts the message before performing payment verification. 

<img src="https://github.com/k4trina/Digital-Wallet/blob/master/PayMo_RSA.PNG" height="80%" width="80%">

Additional security features can naturally be extended from here. Symmetric AES encryption can be performed prior to assymetric RSA encryption. Furthermore, messages sent from PayMo the receiving user can also be encrypted using the receiving user's public key. This implementation is beyond the scope of this project, but noted here as a possible feature. 

