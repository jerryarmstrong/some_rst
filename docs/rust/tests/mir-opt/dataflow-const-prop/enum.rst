tests/mir-opt/dataflow-const-prop/enum.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

// Not trackable, because variants could be aliased.
enum E {
    V1(i32),
    V2(i32)
}

// EMIT_MIR enum.main.DataflowConstProp.diff
fn main() {
    let e = E::V1(0);
    let x = match e { E::V1(x) => x, E::V2(x) => x };
}


