def main():
    t = int(input())
    # for item in range(t):

def zeroes(num, base):
    zeroes = 0
    while num > base:
        num //= base
        zeroes += num
    return zeroes

def emenary(n, m):
    """
    """
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, m)
        nums.append(str(r))
    return ''.join(reversed(nums))

if __name__ == '__main__':
    # print(emenary(720, 3))
    # print(emenary(150, 8))
    # print(emenary(150, 16))
    print(zeroes(6, 3))
    print(zeroes(6, 10))
    print(zeroes(15, 10))
