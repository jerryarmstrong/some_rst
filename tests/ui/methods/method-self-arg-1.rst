tests/ui/methods/method-self-arg-1.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test method calls with self as an argument cannot subvert type checking.

struct Foo;

impl Foo {
    fn bar(&self) {}
}

fn main() {
    let x = Foo;
    Foo::bar(x); //~  ERROR mismatched types
                 //~| expected `&Foo`, found struct `Foo`
    Foo::bar(&42); //~  ERROR mismatched types
                      //~| expected struct `Foo`, found integer
                      //~| expected reference `&Foo`
                      //~| found reference `&{integer}`
}


