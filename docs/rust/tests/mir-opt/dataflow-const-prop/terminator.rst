tests/mir-opt/dataflow-const-prop/terminator.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: DataflowConstProp

fn foo(n: i32) {}

// EMIT_MIR terminator.main.DataflowConstProp.diff
fn main() {
    let a = 1;
    // Checks that we propagate into terminators.
    foo(a + 1);
}


