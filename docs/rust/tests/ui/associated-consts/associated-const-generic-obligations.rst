tests/ui/associated-consts/associated-const-generic-obligations.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    type Out: Sized;
}

impl Foo for String {
    type Out = String;
}

trait Bar: Foo {
    const FROM: Self::Out;
}

impl<T: Foo> Bar for T {
    const FROM: &'static str = "foo";
    //~^ ERROR implemented const `FROM` has an incompatible type for trait [E0326]
}

fn main() {}


