import random
import sys

def main():
    if len(sys.argv) != 2:
        print >> sys.stderr, "Usage: %s <elem_count>" % sys.argv[0]
        exit(-1)

    count = int(sys.argv[1])
    random.seed()

    with open('vec_gen.out', 'w') as file:
        for i in xrange(count):
            r = random.randrange(2**31)
            file.write('%d\n' % r)

if __name__ == '__main__':
    main()
