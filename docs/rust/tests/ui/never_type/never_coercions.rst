tests/ui/never_type/never_coercions.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that having something of type ! doesn't screw up type-checking and that it coerces to the
// LUB type of the other match arms.

fn main() {
    let v: Vec<u32> = Vec::new();
    match 0u32 {
        0 => &v,
        1 => return,
        _ => &v[..],
    };
}


