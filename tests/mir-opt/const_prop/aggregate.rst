tests/mir-opt/const_prop/aggregate.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: ConstProp
// compile-flags: -O

// EMIT_MIR aggregate.main.ConstProp.diff
// EMIT_MIR aggregate.main.PreCodegen.after.mir
fn main() {
    let x = (0, 1, 2).1 + 0;
}


