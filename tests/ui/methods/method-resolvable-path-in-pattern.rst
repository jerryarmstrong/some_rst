tests/ui/methods/method-resolvable-path-in-pattern.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

trait MyTrait {
    fn trait_bar() {}
}

impl MyTrait for Foo {}

fn main() {
    match 0u32 {
        <Foo as MyTrait>::trait_bar => {}
        //~^ ERROR expected unit struct, unit variant or constant, found associated function
    }
}


