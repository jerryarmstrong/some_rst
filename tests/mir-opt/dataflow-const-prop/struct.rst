tests/mir-opt/dataflow-const-prop/struct.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

struct S(i32);

// EMIT_MIR struct.main.DataflowConstProp.diff
fn main() {
    let mut s = S(1);
    let a = s.0 + 2;
    s.0 = 3;
    let b = a + s.0;
}


