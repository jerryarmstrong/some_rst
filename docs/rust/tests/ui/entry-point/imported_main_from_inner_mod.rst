tests/ui/entry-point/imported_main_from_inner_mod.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(imported_main)]

pub mod foo {
    pub fn bar() {
        println!("Hello world!");
    }
}
use foo::bar as main;


