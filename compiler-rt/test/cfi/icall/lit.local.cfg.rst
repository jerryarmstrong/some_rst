compiler-rt/test/cfi/icall/lit.local.cfg.py
===========================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    # The cfi-icall checker is only supported on x86 and x86_64 for now.
if config.root.host_arch not in ['x86', 'x86_64']:
  config.unsupported = True


