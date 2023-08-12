tests/ui/derives/deriving-primitive.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(FromPrimitive)] //~ ERROR cannot find derive macro `FromPrimitive` in this scope
                         //~| ERROR cannot find derive macro `FromPrimitive` in this scope
enum Foo {}

fn main() {}


