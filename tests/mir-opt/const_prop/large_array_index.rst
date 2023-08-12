tests/mir-opt/const_prop/large_array_index.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR_FOR_EACH_BIT_WIDTH

// EMIT_MIR large_array_index.main.ConstProp.diff
fn main() {
    // check that we don't propagate this, because it's too large
    let x: u8 = [0_u8; 5000][2];
}


