tests/ui/impl-trait/generic-with-implicit-hrtb-without-dyn.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: edition2015 edition2021
//[edition2021]edition:2021

#![allow(warnings)]

fn ice() -> impl AsRef<Fn(&())> {
    //[edition2015]~^ ERROR: the trait bound `(): AsRef<(dyn for<'a> Fn(&'a ()) + 'static)>` is not satisfied [E0277]
    //[edition2021]~^^ ERROR: trait objects must include the `dyn` keyword [E0782]
    todo!()
}

fn main() {}


