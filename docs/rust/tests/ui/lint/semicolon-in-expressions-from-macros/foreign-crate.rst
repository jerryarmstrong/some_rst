tests/ui/lint/semicolon-in-expressions-from-macros/foreign-crate.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:foreign-crate.rs
// check-pass

extern crate foreign_crate;

// Test that we do not lint for a macro in a foreign crate
fn main() {
    let _ = foreign_crate::my_macro!();
}


