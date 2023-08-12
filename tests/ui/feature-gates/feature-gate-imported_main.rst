tests/ui/feature-gates/feature-gate-imported_main.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod foo {
    pub fn bar() {
        println!("Hello world!");
    }
}
use foo::bar as main; //~ ERROR using an imported function as entry point


