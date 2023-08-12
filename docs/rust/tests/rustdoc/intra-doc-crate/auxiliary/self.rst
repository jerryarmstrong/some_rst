tests/rustdoc/intra-doc-crate/auxiliary/self.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "cross_crate_self"]

/// Link to [Self]
/// Link to [crate]
pub struct S;

impl S {
    /// Link to [Self::f]
    pub fn f() {}
}


