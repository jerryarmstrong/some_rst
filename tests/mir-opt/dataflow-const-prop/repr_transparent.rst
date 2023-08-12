tests/mir-opt/dataflow-const-prop/repr_transparent.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

// The struct has scalar ABI, but is not a scalar type.
// Make sure that we handle this correctly.
#[repr(transparent)]
struct I32(i32);

// EMIT_MIR repr_transparent.main.DataflowConstProp.diff
fn main() {
    let x = I32(0);
    let y = I32(x.0 + x.0);
}


