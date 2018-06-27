#!/usr/bin/python3
import sys
import os
import unittest
from src.demo import Demo

def help():
    print("""
syntax: %s ARG

where ARG:
  demo one [args]   : run demo one, population count
  demo two [args]   : run demo two, max subarray
  test              : run tests
""" % (os.path.basename(__file__)))

if __name__ == '__main__':

    if len(sys.argv) > 1:
        d = Demo()
        arg = sys.argv[1]
        args = sys.argv[2:]
        if arg == "test":
            print("# running tests")
            suite = unittest.TestLoader().discover('./test')
            runner = unittest.TextTestRunner()
            runner.run(suite)
        elif arg == "demo":
            print("# running demo")
            d.process(args)
        else:
            help()
            print("unsupported arg %r!" % (str(arg)))
    else:
        help()
        print("missing arg!")

