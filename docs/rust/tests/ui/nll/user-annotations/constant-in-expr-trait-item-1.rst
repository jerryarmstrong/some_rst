tests/ui/nll/user-annotations/constant-in-expr-trait-item-1.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo<'a> {
    const C: &'a u32;
}

impl<'a, T> Foo<'a> for T {
    const C: &'a u32 = &22;
}

fn foo<'a>(_: &'a u32) -> &'static u32 {
    <() as Foo<'a>>::C //~ ERROR
}

fn main() {
}


