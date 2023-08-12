tests/ui/closures/binder/nested-closures-regions.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(closure_lifetime_binder)]
#![feature(rustc_attrs)]

#[rustc_regions]
fn main() {
    for<'a> || -> () { for<'c> |_: &'a ()| -> () {}; };
}


