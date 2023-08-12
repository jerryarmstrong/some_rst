llvm/test/tools/llvm-reduce/remove-bbs-sequence.py
==================================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    import subprocess
import sys

opt = subprocess.run( [ 'opt', '-passes=print<loops>','-disable-output', sys.argv[1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE )

stdout = opt.stdout.decode()

pattern = 'Loop at depth 1 containing'

if (pattern in opt.stderr.decode()):
  print('This is interesting!')
  sys.exit(0)
else:
  print('This is NOT interesting!')
  sys.exit(1)


