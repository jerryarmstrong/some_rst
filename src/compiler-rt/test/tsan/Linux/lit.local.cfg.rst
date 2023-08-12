src/compiler-rt/test/tsan/Linux/lit.local.cfg.py
================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    def getRoot(config):
  if not config.parent:
    return config
  return getRoot(config.parent)

root = getRoot(config)

if root.host_os not in ['Linux']:
  config.unsupported = True


