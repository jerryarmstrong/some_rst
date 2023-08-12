tests/ui/suggestions/issue-104086-suggest-let.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    x = x = x;
    //~^ ERROR cannot find value `x` in this scope
    //~| ERROR cannot find value `x` in this scope
    //~| ERROR cannot find value `x` in this scope

    x = y = y = y;
    //~^ ERROR cannot find value `y` in this scope
    //~| ERROR cannot find value `y` in this scope
    //~| ERROR cannot find value `y` in this scope
    //~| ERROR cannot find value `x` in this scope

    x = y = y;
    //~^ ERROR cannot find value `x` in this scope
    //~| ERROR cannot find value `y` in this scope
    //~| ERROR cannot find value `y` in this scope

    x = x = y;
    //~^ ERROR cannot find value `x` in this scope
    //~| ERROR cannot find value `x` in this scope
    //~| ERROR cannot find value `y` in this scope

    x = x; // will suggest add `let`
    //~^ ERROR cannot find value `x` in this scope
    //~| ERROR cannot find value `x` in this scope

    x = y // will suggest add `let`
    //~^ ERROR cannot find value `x` in this scope
    //~| ERROR cannot find value `y` in this scope
}


