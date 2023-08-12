tests/ui/nll/generator-upvar-mutability.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that generators respect the muatability of their upvars.

#![feature(generators)]

fn mutate_upvar() {
    let x = 0;
    move || {
        x = 1;
        //~^ ERROR
        yield;
    };
}

fn main() {}


