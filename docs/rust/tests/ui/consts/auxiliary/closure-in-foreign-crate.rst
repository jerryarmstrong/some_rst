tests/ui/consts/auxiliary/closure-in-foreign-crate.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(const_closures, const_trait_impl)]
#![allow(incomplete_features)]

pub const fn test() {
    let cl = const || {};
    cl();
}


