tests/rustdoc-ui/intra-doc/assoc-mod-inner-outer.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Traits in scope are collected for doc links in both outer and inner module attributes.

// check-pass
// aux-build: assoc-mod-inner-outer-dep.rs

extern crate assoc_mod_inner_outer_dep;
pub use assoc_mod_inner_outer_dep::*;

#[derive(Clone)]
pub struct Struct;

pub mod outer1 {
    /// [crate::Struct::clone]
    pub mod inner {}
}

pub mod outer2 {
    //! [crate::Struct::clone]
}


