def diagonalDifference(arr):
    m_dia=0
    n_dia=0
    n=len(arr[0])-1

    for i in range(len(arr)):
        m_dia=m_dia+arr[i][i]
        n_dia=n_dia+arr[i][n]
        n=n-1
    return abs(m_dia-n_dia)

size=int(input())
arr=list()
