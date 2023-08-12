tests/ui/associated-consts/associated-const-impl-wrong-lifetime.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    const NAME: &'static str;
}


impl<'a> Foo for &'a () {
    const NAME: &'a str = "unit";
    //~^ ERROR const not compatible with trait
}

fn main() {}


