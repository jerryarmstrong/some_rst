tests/ui/issues/issue-64792-bad-unicode-ctor.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct X {}

const Y: X = X("ö"); //~ ERROR expected function, tuple struct or tuple variant, found struct `X`

fn main() {}


