class Fib:
    def __init__(self):
        # initialize memo
        self.memo = {}
        


    def fib(self, n: int) -> int:
        # base case
        if n < 2:
            return n

        # check if fib(n) is already in memo - f(n) was calculated before
        if n in self.memo:
            return self.memo[n]
        else:
            f = self.fib(n - 1) + self.fib(n - 2)

        # store the value of fib(n) when calculated
        self.memo[n] = f

        return f