tests/mir-opt/dataflow-const-prop/cast.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

// EMIT_MIR cast.main.DataflowConstProp.diff
fn main() {
    let a = 257;
    let b = a as u8 + 1;
}


