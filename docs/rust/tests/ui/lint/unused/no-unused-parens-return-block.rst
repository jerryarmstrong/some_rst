tests/ui/lint/unused/no-unused-parens-return-block.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(unused_parens)]
#![allow(unreachable_code)]

fn main() {
    match (return) {} // ok
    if (return) {} // ok
}


