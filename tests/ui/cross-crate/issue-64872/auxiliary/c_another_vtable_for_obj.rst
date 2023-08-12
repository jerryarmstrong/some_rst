tests/ui/cross-crate/issue-64872/auxiliary/c_another_vtable_for_obj.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
// compile-flags: -C debuginfo=2
#![crate_type="rlib"]

extern crate b_reexport_obj;
use b_reexport_obj::Object;

pub fn another_dyn_debug() {
    let ref u = 1_u32;
    let _d = &u as &dyn crate::Object;
    _d.method()
}


