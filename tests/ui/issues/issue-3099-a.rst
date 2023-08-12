tests/ui/issues/issue-3099-a.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum A { B, C }

enum A { D, E } //~ ERROR the name `A` is defined multiple times

fn main() {}


