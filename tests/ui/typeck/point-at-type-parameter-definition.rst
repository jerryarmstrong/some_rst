tests/ui/typeck/point-at-type-parameter-definition.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Trait {
    fn do_stuff(&self);
}

struct Hello;

impl Hello {
    fn method(&self) {}
}

impl<Hello> Trait for Vec<Hello> {
    fn do_stuff(&self) {
        self[0].method(); //~ ERROR no method named `method` found for type parameter `Hello` in the current scope
    }
}

fn main() {}


