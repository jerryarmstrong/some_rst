tests/ui/traits/bound/on-structs-and-enums-locals.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait {
    fn dummy(&self) { }
}

struct Foo<T:Trait> {
    x: T,
}

fn main() {
    let foo = Foo {
        x: 3
    //~^ ERROR E0277
    };

    let baz: Foo<usize> = loop { };
    //~^ ERROR E0277
}


