tests/mir-opt/dataflow-const-prop/tuple.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

// EMIT_MIR tuple.main.DataflowConstProp.diff
fn main() {
    let mut a = (1, 2);
    let b = a.0 + a.1 + 3;
    a = (2, 3);
    let c = a.0 + a.1 + b;
}


