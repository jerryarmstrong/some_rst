tests/ui/derive-uninhabited-enum-38885.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Wunused

// ensure there are no special warnings about uninhabited types
// when deriving Debug on an empty enum

#[derive(Debug)]
enum Void {}

#[derive(Debug)]
enum Foo {
    Bar(u8),
    Void(Void), //~ WARN variant `Void` is never constructed
}

fn main() {
    let x = Foo::Bar(42);
    println!("{:?}", x);
}


