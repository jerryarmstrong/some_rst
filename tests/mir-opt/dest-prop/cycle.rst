tests/mir-opt/dest-prop/cycle.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Tests that cyclic assignments don't hang DestinationPropagation, and result in reasonable code.
// unit-test: DestinationPropagation
fn val() -> i32 {
    1
}

// EMIT_MIR cycle.main.DestinationPropagation.diff
fn main() {
    let mut x = val();
    let y = x;
    let z = y;
    x = z;

    drop(x);
}


