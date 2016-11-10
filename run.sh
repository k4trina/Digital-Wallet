#!/usr/bin/env bash

# I'll execute my programs, with the input directory paymo_input and output the files in the directory paymo_output
#python ./src/antifraud.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output1.txt ./paymo_output/output2.txt ./paymo_output/output3.txt


# Each feature has a single execution line:
python ./src/feature1.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output1.txt
python ./src/feature2.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output2.txt
python ./src/feature3.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output3.txt
python ./src/feature4.py ./paymo_input/batch_payment.txt ./paymo_input/stream_payment.txt ./paymo_output/output4.txt

