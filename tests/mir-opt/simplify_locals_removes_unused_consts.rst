tests/mir-opt/simplify_locals_removes_unused_consts.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // unit-test: SimplifyLocals-before-const-prop
// compile-flags: -C overflow-checks=no

fn use_zst(_: ((), ())) {}

struct Temp {
    x: u8,
}

fn use_u8(_: u8) {}

// EMIT_MIR simplify_locals_removes_unused_consts.main.SimplifyLocals-before-const-prop.diff
fn main() {
    let ((), ()) = ((), ());
    use_zst(((), ()));

    use_u8((Temp { x: 40 }).x + 2);
}


