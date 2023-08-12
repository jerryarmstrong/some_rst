tests/ui/try-block/try-block-catch.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2018

#![feature(try_blocks)]

fn main() {
    let res: Option<bool> = try {
        true
    } catch { };
    //~^ ERROR keyword `catch` cannot follow a `try` block
}


