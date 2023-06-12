    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
    '''
       which leads to a proble about the computation-measurment about C, C m-1(m+n-2) = fac(m+n-2)/fac(n-1)/fac(m-1)
    '''
