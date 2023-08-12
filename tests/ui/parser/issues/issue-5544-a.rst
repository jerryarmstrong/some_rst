tests/ui/parser/issues/issue-5544-a.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let __isize = 340282366920938463463374607431768211456; // 2^128
    //~^ ERROR integer literal is too large
}


