src/doc/unstable-book/src/compiler-flags/unsound-mir-opts.md
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `unsound-mir-opts`

--------------------

The `-Zunsound-mir-opts` compiler flag enables [MIR optimization passes] which can cause unsound behavior.
This flag should only be used by MIR optimization tests in the rustc test suite.

[MIR optimization passes]: https://rustc-dev-guide.rust-lang.org/mir/optimizations.html


