tests/mir-opt/const_prop/mutable_variable_aggregate_partial_read.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test
// compile-flags: -O

// EMIT_MIR mutable_variable_aggregate_partial_read.main.ConstProp.diff
fn main() {
    let mut x: (i32, i32) = foo();
    x.1 = 99;
    x.0 = 42;
    let y = x.1;
}

#[inline(never)]
fn foo() -> (i32, i32) {
    unimplemented!()
}


