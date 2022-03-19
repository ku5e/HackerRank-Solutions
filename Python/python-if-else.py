#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: 02/18/2022
#Purpose: /py-if-else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
	n = int(input().strip())
	if n % 2 == 0:
		if n <= 5:
			print('Not Weird')
		elif n <= 20:
			print('Weird')
		else:
			print('Not Weird')
	else: 
		print('Weird')