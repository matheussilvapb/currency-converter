#!/usr/bin/env python

from sys import argv

from ui import *
from request import *

if __name__ == "__main__":

    try:
        if argv[1] == "--help":
            print_help(argv[0])
        elif argv[1] == "-l":
            print_currencies()
        else:
            try:
                rate = get_rate(argv[1], argv[2])
            except KeyError:
                print("Currency not available, type '" + argv[0] + " -l' to " +
                        "get a list of the available currencies")
            else:
                print_rate(rate, argv[1], argv[2])
    except IndexError:
        print("Type '" + argv[0] + " --help' to know how to use it")