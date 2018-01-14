import sys


def MatrixChainOrder(p, n):

    m = [[0 for x in range(n)] for x in range(n)]


    # L is chain length.
    for L in range(2, n+1):
        for i in range(1, n - L + 1):
            j = i + L - 1
            m[i][j] = -1*sys.maxint
            for k in range(i, j):

                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q > m[i][j]:
                    m[i][j] = q

    print m
    return m[1][n-1]

arr = [30, 35, 15, 5,10,25]
size = len(arr)

print("Maximum number of multiplications is " +
      str(MatrixChainOrder(arr, size)))