tests/ui/nll/user-annotations/constant-in-expr-inherent-1.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<'a> { x: &'a u32 }

impl<'a> Foo<'a> {
    const C: &'a u32 = &22;
}

fn foo<'a>(_: &'a u32) -> &'static u32 {
    <Foo<'a>>::C //~ ERROR
}

fn main() {
}


