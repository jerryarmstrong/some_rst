src/compiler-rt/test/asan/TestCases/Windows/lit.local.cfg.py
============================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    def getRoot(config):
  if not config.parent:
    return config
  return getRoot(config.parent)

root = getRoot(config)

# We only run a small set of tests on Windows for now.
# Override the parent directory's "unsupported" decision until we can handle
# all of its tests.
if root.host_os in ['Windows']:
  config.unsupported = False
else:
  config.unsupported = True


