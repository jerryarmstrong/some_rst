tests/ui/macros/macro-export-inner-module.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
//aux-build:macro_export_inner_module.rs

#[macro_use] #[no_link]
extern crate macro_export_inner_module;

pub fn main() {
    assert_eq!(1, foo!());
}


