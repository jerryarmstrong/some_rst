src/compiler-rt/test/asan/TestCases/Android/lit.local.cfg.py
============================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    def getRoot(config):
  if not config.parent:
    return config
  return getRoot(config.parent)

root = getRoot(config)

if root.android != "1":
  config.unsupported = True

config.substitutions.append( ("%device", "/data/local/tmp/Output") )


