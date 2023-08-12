tests/ui/deref-patterns/default-infer.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![feature(string_deref_patterns)]

fn main() {
    match <_ as Default>::default() {
        "" => (),
        _ => unreachable!(),
    }
}


