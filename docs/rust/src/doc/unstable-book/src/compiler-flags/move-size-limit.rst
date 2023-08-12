src/doc/unstable-book/src/compiler-flags/move-size-limit.md
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: md

    # `move_size_limit`

--------------------

The `-Zmove-size-limit=N` compiler flag enables `large_assignments` lints which
will warn when moving objects whose size exceeds `N` bytes.

Lint warns only about moves in functions that participate in code generation.
Consequently it will be ineffective for compiler invocatation that emit
metadata only, i.e., `cargo check` like workflows.


