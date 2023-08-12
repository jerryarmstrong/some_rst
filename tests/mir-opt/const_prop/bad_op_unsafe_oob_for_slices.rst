tests/mir-opt/const_prop/bad_op_unsafe_oob_for_slices.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR_FOR_EACH_BIT_WIDTH
// EMIT_MIR bad_op_unsafe_oob_for_slices.main.ConstProp.diff
#[allow(unconditional_panic)]
fn main() {
    let a: *const [_] = &[1, 2, 3];
    unsafe {
        let _b = (*a)[3];
    }
}


