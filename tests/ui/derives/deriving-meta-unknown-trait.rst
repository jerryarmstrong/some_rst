tests/ui/derives/deriving-meta-unknown-trait.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Eqr)]
//~^ ERROR cannot find derive macro `Eqr` in this scope
//~| ERROR cannot find derive macro `Eqr` in this scope
struct Foo;

pub fn main() {}


