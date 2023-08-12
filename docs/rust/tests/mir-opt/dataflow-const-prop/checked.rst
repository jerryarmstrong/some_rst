tests/mir-opt/dataflow-const-prop/checked.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp
// compile-flags: -Coverflow-checks=on

// EMIT_MIR checked.main.DataflowConstProp.diff
#[allow(arithmetic_overflow)]
fn main() {
    let a = 1;
    let b = 2;
    let c = a + b;

    let d = i32::MAX;
    let e = d + 1;
}


