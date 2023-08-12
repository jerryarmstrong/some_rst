tests/mir-opt/dataflow-const-prop/ref_without_sb.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

#[inline(never)]
fn escape<T>(x: &T) {}

#[inline(never)]
fn some_function() {}

// EMIT_MIR ref_without_sb.main.DataflowConstProp.diff
fn main() {
    let mut a = 0;
    escape(&a);
    a = 1;
    some_function();
    // This should currently not be propagated.
    let b = a;
}


