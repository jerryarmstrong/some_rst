tests/ui/issues/issue-7044.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static X: isize = 0;
struct X; //~ ERROR the name `X` is defined multiple times

fn main() {}


