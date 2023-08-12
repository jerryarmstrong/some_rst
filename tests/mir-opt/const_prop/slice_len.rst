tests/mir-opt/const_prop/slice_len.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zmir-enable-passes=-SimplifyLocals-before-const-prop
// EMIT_MIR_FOR_EACH_BIT_WIDTH

// EMIT_MIR slice_len.main.ConstProp.diff
fn main() {
    (&[1u32, 2, 3] as &[u32])[1];
}


