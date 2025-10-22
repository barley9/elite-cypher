def l_josephus(n):
    b = bin(n)          # store the binary string representation of n
    l = len(b)          # store the length of bin(n)
    pos = l - 3         # store the position of the first nonzero digit of bin(n)
    power = 2**pos      # convert 'pos' into its corresponding numerical value
    sub = n - power     # subtract off the leading nonzero digit of n
    a = bin(sub)        # convert that difference back to binary
    new = a + '1'       # append a '1' to the end of that string representation
    final = int(new, 2) # convert that base-2 string to an integer
    return final        # This function uses O(1) instead of the naive O(n^2)


if __name__ == '__main__':
    for i in range(1, 20):
        print(i, l_josephus(i))
