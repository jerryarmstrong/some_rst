tests/ui/try-block/try-block-in-return.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --edition 2018

#![feature(try_blocks)]

fn issue_76271() -> Option<i32> {
    return try { 4 }
}

fn main() {
    assert_eq!(issue_76271(), Some(4));
}


