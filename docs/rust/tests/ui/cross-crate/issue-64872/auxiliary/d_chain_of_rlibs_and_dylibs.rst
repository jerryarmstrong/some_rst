tests/ui/cross-crate/issue-64872/auxiliary/d_chain_of_rlibs_and_dylibs.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C debuginfo=2 -C prefer-dynamic

#![crate_type="rlib"]

extern crate c_another_vtable_for_obj;

pub fn chain() {
    c_another_vtable_for_obj::another_dyn_debug();
}


