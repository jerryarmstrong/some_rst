tests/ui/generator/too-many-parameters.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

fn main() {
    |(), ()| {
        //~^ error: too many parameters for a generator
        yield;
    };
}


