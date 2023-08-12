tests/ui/inline-const/expr-with-block.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(inline_const)]
fn main() {
    match true {
        true => const {}
        false => ()
    }
    const {}
    ()
}


