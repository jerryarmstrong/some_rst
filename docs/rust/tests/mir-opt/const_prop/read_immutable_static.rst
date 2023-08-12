tests/mir-opt/const_prop/read_immutable_static.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test
// compile-flags: -O

static FOO: u8 = 2;

// EMIT_MIR read_immutable_static.main.ConstProp.diff
fn main() {
    let x = FOO + FOO;
}


