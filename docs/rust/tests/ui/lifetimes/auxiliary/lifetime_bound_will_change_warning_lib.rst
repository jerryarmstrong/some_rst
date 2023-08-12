tests/ui/lifetimes/auxiliary/lifetime_bound_will_change_warning_lib.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "rlib"]

// Helper for testing that we get suitable warnings when lifetime
// bound change will cause breakage.

pub fn just_ref(x: &Fn()) {
}

pub fn ref_obj(x: &Box<Fn()>) {
    // this will change to &Box<Fn()+'static>...
}


