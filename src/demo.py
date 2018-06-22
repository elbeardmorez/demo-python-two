import sys


def population_count(count):
    return len(str(bin(int(count)))[2:].replace('0', ''))


def test():
    tests = [(0, 0), (8, 1), (15, 4), (19, 3)]
    try:
        for t, target in tests:
            print("testing 'population_count(%d): " % (t), end="")
            res = population_count(t)
            success = res == target
            if not success:
                raise AssertionError("incorrect result")
            print("%d : %s" % (res, "[success]"))
    except AssertionError as e:
        print("n/a : [failure | %s]" % (e))


def help():
    print("""
syntax: %s ARG

where ARG:
  [0-9]+  : arbitrary positive integer
  test    : to invoke tests
""" % (__file__))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg.isdigit():
            print("population_count: '%d'" % (population_count(arg)))
        elif arg == "test":
            # too trivial for suite
            test()
    else:
        help()
        print("missing arg!")
