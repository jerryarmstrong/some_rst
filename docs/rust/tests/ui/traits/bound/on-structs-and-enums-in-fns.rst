tests/ui/traits/bound/on-structs-and-enums-in-fns.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait {}

struct Foo<T:Trait> {
    x: T,
}

enum Bar<T:Trait> {
    ABar(isize),
    BBar(T),
    CBar(usize),
}

fn explode(x: Foo<u32>) {}
//~^ ERROR E0277

fn kaboom(y: Bar<f32>) {}
//~^ ERROR E0277

fn main() {
}


