import sys


def population_count(count):
    return len(str(bin(int(count)))[2:].replace('0', ''))


def test():
    tests = [(0, 0), (8, 1), (15, 4), (19, 3)]
    try:
        for t, target in tests:
            print("testing 'population_count(%d): " % (t), end="")
            res = population_count(t)
            assert res == target, "incorrect result"
            print("%d : %s" % (res, "[success]"))
    except Exception as e:
        print("n/a : [failure | %s]" % (e))

def max_sum_of_subarray(l):
    smax = -100
    for idx in range(len(l)):
        _sum = 0
        for idx2 in range(idx, len(l)):
            _sum += l[idx2]
            if _sum > smax:
                smax = _sum
    print("max subarray size: %d" % smax)

def help():
    print("""
syntax: %s ARG

where ARG:
  [0-9]+  : arbitrary positive integer
  test    : to invoke tests
""" % (__file__))


if __name__ == '__main__':

    while True:
        s = input().split()
        if s == "":
            break;
        l = [int(x) for x in s]
        max_sum_of_subarray(l)

    sys.exit()

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
