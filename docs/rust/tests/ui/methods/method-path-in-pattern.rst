tests/ui/methods/method-path-in-pattern.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo;

impl Foo {
    fn bar(&self) {}
}

trait MyTrait {
    fn trait_bar() {}
}

impl MyTrait for Foo {}

fn main() {
    match 0u32 {
        Foo::bar => {}
        //~^ ERROR expected unit struct, unit variant or constant, found associated function
    }
    match 0u32 {
        <Foo>::bar => {}
        //~^ ERROR expected unit struct, unit variant or constant, found associated function
    }
    match 0u32 {
        <Foo>::trait_bar => {}
        //~^ ERROR expected unit struct, unit variant or constant, found associated function
    }
    if let Foo::bar = 0u32 {}
    //~^ ERROR expected unit struct, unit variant or constant, found associated function
    if let <Foo>::bar = 0u32 {}
    //~^ ERROR expected unit struct, unit variant or constant, found associated function
    if let Foo::trait_bar = 0u32 {}
    //~^ ERROR expected unit struct, unit variant or constant, found associated function
}


