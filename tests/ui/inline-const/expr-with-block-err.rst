tests/ui/inline-const/expr-with-block-err.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(inline_const)]

fn main() {
    const { 2 } - const { 1 };
    //~^ ERROR mismatched types
}


