tests/mir-opt/const_prop/bad_op_div_by_zero.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: ConstProp
// EMIT_MIR bad_op_div_by_zero.main.ConstProp.diff
#[allow(unconditional_panic)]
fn main() {
    let y = 0;
    let _z = 1 / y;
}


