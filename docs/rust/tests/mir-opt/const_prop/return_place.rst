tests/mir-opt/const_prop/return_place.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C overflow-checks=on

// EMIT_MIR return_place.add.ConstProp.diff
// EMIT_MIR return_place.add.PreCodegen.before.mir
fn add() -> u32 {
    2 + 2
}

fn main() {
    add();
}


