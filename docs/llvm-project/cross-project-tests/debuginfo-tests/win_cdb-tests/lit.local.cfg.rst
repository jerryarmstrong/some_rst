cross-project-tests/debuginfo-tests/win_cdb-tests/lit.local.cfg.py
==================================================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    # The win_cdb tests are supported when cmake was run in an MSVC environment.
config.unsupported = not config.is_msvc


