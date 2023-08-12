tests/ui/entry-point/imported_main_from_extern_crate.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:main_functions.rs

#![feature(imported_main)]

extern crate main_functions;
pub use main_functions::boilerplate as main;


