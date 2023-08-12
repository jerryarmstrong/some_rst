tests/ui/nll/user-annotations/constant-in-expr-normalize.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Mirror {
    type Me;
}

impl<T> Mirror for T {
    type Me = T;
}

trait Foo<'a> {
    const C: <&'a u32 as Mirror>::Me;
}

impl<'a, T> Foo<'a> for T {
    const C: &'a u32 = &22;
}

fn foo<'a>(_: &'a u32) -> &'static u32 {
    <() as Foo<'a>>::C //~ ERROR
}

fn main() {
}


