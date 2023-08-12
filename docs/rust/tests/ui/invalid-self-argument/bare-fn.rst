tests/ui/invalid-self-argument/bare-fn.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn b(foo: u32, &mut self) { }
//~^ ERROR unexpected `self` parameter in function
//~| NOTE must be the first parameter of an associated function

fn main() { }


