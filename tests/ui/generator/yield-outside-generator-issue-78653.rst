tests/ui/generator/yield-outside-generator-issue-78653.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

fn main() {
    yield || for i in 0 { }
    //~^ ERROR yield expression outside of generator literal
    //~| ERROR `{integer}` is not an iterator
}


