tests/ui/inline-const/const-expr-macro.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![feature(inline_const)]

macro_rules! do_const_block{
    ($val:block) => { const $val }
}

fn main() {
    let s = do_const_block!({ 22 });
    assert_eq!(s, 22);
}


