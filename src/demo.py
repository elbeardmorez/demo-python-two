import sys

class Demo:

    def help_population_count(self):
        print("""
syntax: %s ARG

where ARG:
  [0-9]+  : arbitrary positive integer
  test    : to invoke tests
""" % (__file__))

    def population_count(self, count):
        return len(str(bin(int(count)))[2:].replace('0', ''))

    def test_population_count(self):
        tests = [(0, 0), (8, 1), (15, 4), (19, 3)]
        try:
            for t, target in tests:
                print("testing 'population_count(%d): " % (t), end="")
                res = self.population_count(t)
                assert res == target, "incorrect result"
                print("%d : %s" % (res, "[success]"))
        except Exception as e:
            print("n/a : [failure | %s]" % (e))

    def largest_subarray(self, l):
        smax = -100
        for idx in range(len(l)):
            _sum = 0
            for idx2 in range(idx, len(l)):
                _sum += l[idx2]
                if _sum > smax:
                    smax = _sum
        return smax

    def test_largest_subarray(self):
        tests = [([1, 2, 4], 7),
                 ([-21, -1, -1, 0], 0),
                 ([1, 2, -10, 3, 100, 1222], 1325),
                 ([-1, -2, -5], -1)]
        try:
            for t, target in tests:
                print("testing 'largest_subarray(%s): "
                      % (" ".join([str(x) for x in t])), end="")
                res = self.largest_subarray(t)
                assert res == target, "incorrect result"
                print("%d : %s" % (res, "[success]"))
        except Exception as e:
            print("n/a : [failure | %s]" % (e))

    def process(self, args):
        if len(args) > 0:
            arg = args[0]
            if arg == "one":
                if len(args) > 1:
                    arg = args[1]
                    if arg.isdigit():
                        print("population_count: '%d'" % (self.population_count(arg)))
                    elif arg == "test":
                        # too trivial for suite
                        self.test_population_count()
            elif arg == "two":
                l = []
                if len(args) > 1:
                    arg = args[1]
                    if arg == "test":
                        # too trivial for suite
                        self.test_largest_subarray()
                    else:
                        l = [int(x) for x in args[1:]]
                        print("largest subarray: %d"
                              % (self.largest_subarray(l)))
                else:
                    print("reading from stdin")
                    lines = sys.stdin.readlines()
                    if len(lines) == 0:
                        self.help_largest_subarray()
                    else:
                        for s in lines:
                            l = [int(x) for x in s.split()]
                            print("largest subarray: %d"
                                  % (self.largest_subarray(l)))

        else:
            self.help()
            print("missing arg!")

if __name__ == '__main__':
    d = Demo()
    d.process(sys.argv[1:])
