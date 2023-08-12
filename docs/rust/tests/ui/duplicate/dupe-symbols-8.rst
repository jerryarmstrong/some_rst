tests/ui/duplicate/dupe-symbols-8.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// error-pattern: entry symbol `main` declared multiple times
//
// See #67946.

#![allow(warnings)]
fn main() {
    extern "Rust" {
     fn main();
    }
    unsafe { main(); }
}


