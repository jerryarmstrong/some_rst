tests/mir-opt/remove_zsts.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    union Foo {
    x: (),
    y: u64,
}

// EMIT_MIR remove_zsts.get_union.RemoveZsts.diff
// EMIT_MIR remove_zsts.get_union.PreCodegen.after.mir
fn get_union() -> Foo {
    Foo { x: () }
}

fn main() {
    get_union();
}


