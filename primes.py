#!/usr/bin/env python

import primefac
import sys

#Intro
print('\n\n\033[1;34mPrimes Factorization \033[00m- version 1.0 \nby \033[1;32m@yunniscan\033[00m')

try:
  n = int( sys.argv[1] )
	factors = list( primefac.primefac(n) )

	if len(factors) == 0:
		print ('\n\033[01;31m' + 'Not Found...' + '\033[00m')
	else:
		print ('\n\033[0;32;47m' + 'Found!' + '\033[000m')

		print ('\n\033[02;37m' + 'Prime 1:' + '\033[00m')
		print factors[0]
		print ('\n\033[02;37m' + 'Prime 2:' + '\033[00m')
		print factors[1]
except:
	print("\n\n\033[1;31m Oops! Something went wrong... Try again... \033[00m\n")
	print("\n \033[33mUsage: \033[1;35mprimes.py <prime_number> \033[00m")
