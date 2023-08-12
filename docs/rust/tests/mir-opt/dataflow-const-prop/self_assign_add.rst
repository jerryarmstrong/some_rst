tests/mir-opt/dataflow-const-prop/self_assign_add.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

// EMIT_MIR self_assign_add.main.DataflowConstProp.diff
fn main() {
    let mut a = 0;
    a += 1;
    a += 1;
}


