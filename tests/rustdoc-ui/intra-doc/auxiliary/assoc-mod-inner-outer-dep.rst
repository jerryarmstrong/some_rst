tests/rustdoc-ui/intra-doc/auxiliary/assoc-mod-inner-outer-dep.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
pub struct Struct;

pub mod dep_outer1 {
    /// [crate::Struct::clone]
    pub mod inner {}
}

pub mod dep_outer2 {
    //! [crate::Struct::clone]
}


