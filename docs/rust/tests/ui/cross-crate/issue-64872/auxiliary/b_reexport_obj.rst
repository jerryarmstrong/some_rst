tests/ui/cross-crate/issue-64872/auxiliary/b_reexport_obj.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C debuginfo=2 -C prefer-dynamic

#![crate_type="dylib"]

extern crate a_def_obj;

pub use a_def_obj::Object;


