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


def assertMySqrt():
    pass

def check_my_sqrt0():
    result = my_sqrt(4)
    expect = 1

    # if result == expect:
    #     print("correct")
    # else:
    #     print("error")

    assert result == expect,"wrong"

def check_my_sqrt1():
    result = my_sqrt(4) * my_sqrt(4)
    expect = 4

    assert result == expect,"wrong"

def check_my_sqrt2():
    result = my_sqrt(4) * my_sqrt(4)
    expect = 4
    epclion = 1e-8

    assert abs(result - expect) < epclion,"wrong"

def assertMySqrt(x,y,epclion=1e-8):
    assert abs(x - y) < epclion,"wrong"


def check_my_sqrt3():
    for i in range(0,1000):
        result = my_sqrt(i) * my_sqrt(i)
        expect = i
        assertMySqrt(result, expect)

def check_my_sqrt4():
    for i in range(1000):
        num = random.random()
        result = my_sqrt(num) * my_sqrt(num)
        expect = num
        assertMySqrt(result,expect)


def check_my_sqrt5():
    arg = int(sys.argv[1])
    if len(sys.argv) < 2:
        print("no enough arguments.")
    try:
        float(arg)
    except ValueError:
        print("Illegal input")
    else:
        if arg < 0:
            print("Illegal input")
        else:
            print(f"result is {my_sqrt(arg)}")

    result = my_sqrt(arg) * my_sqrt(arg)
    expect = arg

    assertMySqrt(result,expect)


def main():
    # check_my_sqrt0()
    # check_my_sqrt1()
    # check_my_sqrt2()
    # check_my_sqrt3()
    # check_my_sqrt4()
    check_my_sqrt5()



if __name__ == "__main__":
     main()