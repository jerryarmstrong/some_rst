tests/ui/invalid-self-argument/bare-fn-start.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a(&self) { }
//~^ ERROR `self` parameter is only allowed in associated functions
//~| NOTE not semantically valid as function parameter
//~| NOTE associated functions are those in `impl` or `trait` definitions

fn main() { }


