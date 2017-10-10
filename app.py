#!/usr/bin/python3

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../system')

import azbn as azbnpy

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

def main():
	
	#help(azbn.echo)
	azbn.echo('It is default educational app for python')

if __name__ == '__main__':
	main()