tests/mir-opt/const_prop/indirect.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: ConstProp
// compile-flags: -C overflow-checks=on

// EMIT_MIR indirect.main.ConstProp.diff
fn main() {
    let x = (2u32 as u8) + 1;
}


