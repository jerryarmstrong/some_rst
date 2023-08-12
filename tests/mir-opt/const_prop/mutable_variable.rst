tests/mir-opt/const_prop/mutable_variable.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test
// compile-flags: -O

// EMIT_MIR mutable_variable.main.ConstProp.diff
fn main() {
    let mut x = 42;
    x = 99;
    let y = x;
}


