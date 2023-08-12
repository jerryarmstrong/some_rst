tests/ui/traits/bound/on-structs-and-enums-in-impls.rs
======================================================

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

trait PolyTrait<T>
{
    fn whatever(&self, t: T) {}
}

struct Struct;

impl PolyTrait<Foo<u16>> for Struct {
//~^ ERROR E0277
}

fn main() {
}


