tests/ui/nll/user-annotations/constant-in-expr-trait-item-3.rs
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

fn foo<'a, T: Foo<'a>>() -> &'static u32 {
    T::C //~ ERROR
}

fn main() {
}


