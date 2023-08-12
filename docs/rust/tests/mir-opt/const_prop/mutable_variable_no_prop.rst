tests/mir-opt/const_prop/mutable_variable_no_prop.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test
// compile-flags: -O

static mut STATIC: u32 = 0x42424242;

// EMIT_MIR mutable_variable_no_prop.main.ConstProp.diff
fn main() {
    let mut x = 42;
    unsafe {
        x = STATIC;
    }
    let y = x;
}


