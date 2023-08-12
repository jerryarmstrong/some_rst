tests/ui/deref-patterns/gate.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // gate-test-string_deref_patterns
fn main() {
    match String::new() {
        "" | _ => {}
        //~^ mismatched types
    }
}


