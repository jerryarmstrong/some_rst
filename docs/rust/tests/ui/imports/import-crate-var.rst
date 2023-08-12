tests/ui/imports/import-crate-var.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:import_crate_var.rs

#[macro_use] extern crate import_crate_var;

fn main() {
    m!();
    //~^ ERROR `$crate` may not be imported
}


