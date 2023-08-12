clang/utils/TestUtils/deep-stack.py
===================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    #!/usr/bin/env python

from __future__ import absolute_import, division, print_function
def pcall(f, N):
    if N == 0:
        print('    f(0)', file=f)
        return

    print('    f(', file=f)
    pcall(f, N - 1)
    print('     )', file=f)

def main():
    f = open('t.c','w')
    print('int f(int n) { return n; }', file=f)
    print('int t() {', file=f)
    print('  return', file=f)
    pcall(f, 10000)
    print('  ;', file=f)
    print('}', file=f)

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(100000)
    main()


