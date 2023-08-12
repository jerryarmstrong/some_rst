tests/ui/suggestions/attribute-typos.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deprcated] //~ ERROR cannot find attribute `deprcated` in this scope
fn foo() {}

#[tests] //~ ERROR cannot find attribute `tests` in this scope
fn bar() {}

#[rustc_err]
//~^ ERROR cannot find attribute `rustc_err` in this scope
//~| ERROR attributes starting with `rustc` are reserved for use by the `rustc` compiler

fn main() {}


