tests/mir-opt/const_prop/repeat.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -O

// EMIT_MIR_FOR_EACH_BIT_WIDTH
// EMIT_MIR repeat.main.ConstProp.diff
fn main() {
    let x: u32 = [42; 8][2] + 0;
}


