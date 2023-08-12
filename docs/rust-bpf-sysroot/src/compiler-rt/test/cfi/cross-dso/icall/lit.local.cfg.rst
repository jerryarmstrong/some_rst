src/compiler-rt/test/cfi/cross-dso/icall/lit.local.cfg.py
=========================================================

Last edited: 2021-03-26 10:45:53

Contents:

.. code-block:: py

    # The cfi-icall checker is only supported on x86 and x86_64 for now.
if config.root.host_arch not in ['x86', 'x86_64']:
  config.unsupported = True


