from fuzzingbook.Timer import Timer
import random
import sys

def my_sqrt(x):
    """Computes the square root of x, using the Newton-Raphson method"""
    if x == 0:
        return 0
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx


def assertEquals(x, y, epsilon=1e-8):
    assert abs(x - y) < epsilon


def check_sqrt():
    with Timer() as t:
        for i in range(10000):
            x = 1 + random.random() * 100000

            result_sqrt = my_sqrt(x) * my_sqrt(x)
            expect_sqrt = x

            assertEquals(result_sqrt,expect_sqrt)
    print(t.elapsed_time())



def main():
    arg = sys.argv[1]
    if len(sys.argv) < 2:
        print("No enough argument.")
    arg = int(arg)
    try:
        arg = float(arg)
    except ValueError:
        print("Illegal input")
    else:
        if arg < 0:
            print("Illegal input")
        else:
            print(f"sqrt result is :{my_sqrt(arg)}")




    # check_sqrt()

if __name__ == "__main__":
    main()