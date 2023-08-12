tests/mir-opt/const_prop/tuple_literal_propagation.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR tuple_literal_propagation.main.ConstProp.diff
fn main() {
    let x = (1, 2);

    consume(x);
}

#[inline(never)]
fn consume(_: (u32, u32)) { }


