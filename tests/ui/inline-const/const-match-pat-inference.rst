tests/ui/inline-const/const-match-pat-inference.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(inline_const_pat)]
#![allow(incomplete_features)]

fn main() {
    match 1u64 {
        0 => (),
        const { 0 + 1 } => (),
        const { 2 - 1 } ..= const { u64::MAX } => (),
    }
}


