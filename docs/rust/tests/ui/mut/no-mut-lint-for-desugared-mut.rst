tests/ui/mut/no-mut-lint-for-desugared-mut.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(unused_mut)]
#![allow(unreachable_code)]

fn main() {
    for _ in { return (); 0..3 } {} // ok
}


