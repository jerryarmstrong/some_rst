tests/rustdoc-ui/assoc-item-not-in-scope.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(rustdoc::broken_intra_doc_links)]

#[derive(Debug)]
/// Link to [`S::fmt`]
//~^ ERROR unresolved link
pub struct S;

pub mod inner {
    use std::fmt::Debug;
    use super::S;

    /// Link to [`S::fmt`]
    pub fn f() {}
}

pub mod ambiguous {
    use std::fmt::{Display, Debug};
    use super::S;

    /// Link to [`S::fmt`]
    pub fn f() {}
}


