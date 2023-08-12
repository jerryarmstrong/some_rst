compiler-rt/test/msan/Linux/lit.local.cfg.py
============================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    def getRoot(config):
  if not config.parent:
    return config
  return getRoot(config.parent)

root = getRoot(config)

if root.host_os not in ['Linux']:
  config.unsupported = True


