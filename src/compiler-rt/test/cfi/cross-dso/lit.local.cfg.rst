src/compiler-rt/test/cfi/cross-dso/lit.local.cfg.py
===================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    def getRoot(config):
  if not config.parent:
    return config
  return getRoot(config.parent)

root = getRoot(config)

if root.host_os not in ['Linux', 'FreeBSD', 'NetBSD']:
  config.unsupported = True

# Android O (API level 26) has support for cross-dso cfi in libdl.so.
if config.android and 'android-26' not in config.available_features:
  config.unsupported = True


