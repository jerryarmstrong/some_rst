tests/mir-opt/const_prop/mutable_variable_aggregate_mut_ref.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test
// compile-flags: -O

// EMIT_MIR mutable_variable_aggregate_mut_ref.main.ConstProp.diff
fn main() {
    let mut x = (42, 43);
    let z = &mut x;
    z.1 = 99;
    let y = x;
}


