tests/mir-opt/spanview_statement.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test spanview output (the default value for `-Z dump-mir-spanview` is "statement")
// compile-flags: -Z dump-mir-spanview

// EMIT_MIR spanview_statement.main.built.after.html
fn main() {}


