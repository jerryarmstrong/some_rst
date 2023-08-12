tests/ui/parser/impl-item-type-no-body-semantic-fail.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

struct X;

impl X {
    type Y;
    //~^ ERROR associated type in `impl` without body
    //~| ERROR inherent associated types are unstable
    type Z: Ord;
    //~^ ERROR associated type in `impl` without body
    //~| ERROR bounds on `type`s in `impl`s have no effect
    //~| ERROR inherent associated types are unstable
    type W: Ord where Self: Eq;
    //~^ ERROR associated type in `impl` without body
    //~| ERROR bounds on `type`s in `impl`s have no effect
    //~| ERROR inherent associated types are unstable
    type W where Self: Eq;
    //~^ ERROR associated type in `impl` without body
    //~| ERROR inherent associated types are unstable
}


