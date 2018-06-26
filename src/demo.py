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
        print("largest subarray: %d" % smax)

    def process(self, args):
        if len(args) > 0:
            arg = sys.argv[0]
            if arg == "one":
                if len(sys.argv) > 1:
                    arg = sys.argv[1]
                    if arg.isdigit():
                        print("population_count: '%d'" % (population_count(arg)))
                    elif arg == "test":
                        # too trivial for suite
                        self.test_population_count()
            elif arg == "two":
                while True:
                    s = input().split()
                    if s == "":
                        break;
                    l = [int(x) for x in s]
                    self.largest_subarray(l)
        else:
            help()
            print("missing arg!")

if __name__ == '__main__':
    d = Demo()
    d.process(sys.argv[1:])
