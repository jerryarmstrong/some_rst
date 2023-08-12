tests/mir-opt/const_prop/array_index.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: ConstProp
// EMIT_MIR_FOR_EACH_BIT_WIDTH

// EMIT_MIR array_index.main.ConstProp.diff
fn main() {
    let x: u32 = [0, 1, 2, 3][2];
}


