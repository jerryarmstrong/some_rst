tests/ui/lint/rustdoc-group.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: --crate-type lib
#![deny(rustdoc)]
//~^ WARNING removed: use `rustdoc::all`
#![deny(rustdoc::all)] // has no effect when run with rustc directly


