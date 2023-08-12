tests/ui/infinite/infinite-type-alias-mutual-recursion.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type X1 = X2;
//~^ ERROR cycle detected when expanding type alias `X1`
type X2 = X3;
type X3 = X1;

fn main() {}


