tests/ui/lto/all-crates.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

// compile-flags: -Clto=thin
// no-prefer-dynamic

fn main() {
    println!("hello!");
}


