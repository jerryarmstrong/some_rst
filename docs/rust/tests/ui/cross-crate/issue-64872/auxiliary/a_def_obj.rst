tests/ui/cross-crate/issue-64872/auxiliary/a_def_obj.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C debuginfo=2

// no-prefer-dynamic
#![crate_type = "rlib"]

pub trait Object { fn method(&self) { } }

impl Object for u32 { }
impl Object for () { }
impl<T> Object for &T { }

pub fn unused() {
    let ref u = 0_u32;
    let _d = &u as &dyn crate::Object;
    _d.method()
}


