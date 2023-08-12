tests/ui/traits/bound/on-structs-and-enums-static.rs
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

static X: Foo<usize> = Foo {
//~^ ERROR E0277
    x: 1,
};

fn main() {
}


