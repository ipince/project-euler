#!/usr/bin/python

from scipy import optimize

# For which f is the expression (1 + 2f)^k * (1 - f)^(n - k) >= C
# klog(1+2f) + (n-k)log(1-f) = log(C)
# 
def solve(n, k, c):
  guesses = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
  func = lambda f, n, k, c : (1+2*f)**k * (1-f)**(n-k) - c
  roots = set()
  for guess in guesses:
    try:
      #root = optimize.newton(func, guess, args=(n, k, c), maxiter=100)
      root = optimize.brentq(func, -1, 1, args=(n, k, c))
      print 'root for %f is %f' % (guess, root)
      if root >= 0 and root <= 1:
        roots.add(root)
    except OverflowError:
      print 'Overflowed with %f' % guess
      continue
  return roots

solve(1000, 500, 1000000000)
