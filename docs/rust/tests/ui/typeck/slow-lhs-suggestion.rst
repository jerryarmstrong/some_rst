tests/ui/typeck/slow-lhs-suggestion.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1 = 1;
    //~^ ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment
}


