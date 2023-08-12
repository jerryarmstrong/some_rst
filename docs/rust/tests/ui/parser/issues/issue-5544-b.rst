tests/ui/parser/issues/issue-5544-b.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let __isize = 0xffff_ffff_ffff_ffff_ffff_ffff_ffff_ffff_ff;
    //~^ ERROR integer literal is too large
}


