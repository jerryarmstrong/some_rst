tests/mir-opt/dataflow-const-prop/inherit_overflow.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zunsound-mir-opts

// EMIT_MIR inherit_overflow.main.DataflowConstProp.diff
fn main() {
    // After inlining, this will contain a `CheckedBinaryOp`. The overflow
    // must be ignored by the constant propagation to avoid triggering a panic.
    let _ = <u8 as std::ops::Add>::add(255, 1);
}


