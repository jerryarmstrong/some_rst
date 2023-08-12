tests/mir-opt/dataflow-const-prop/self_assign.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

// EMIT_MIR self_assign.main.DataflowConstProp.diff
fn main() {
    let mut a = 0;
    a = a + 1;
    a = a;

    let mut b = &a;
    b = b;
    a = *b;
}


