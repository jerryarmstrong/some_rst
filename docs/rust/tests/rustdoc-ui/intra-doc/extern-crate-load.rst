tests/rustdoc-ui/intra-doc/extern-crate-load.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-crate:dep1=dep1.rs
// aux-crate:dep2=dep2.rs
// aux-crate:dep3=dep3.rs
// aux-crate:dep4=dep4.rs
#![deny(rustdoc::broken_intra_doc_links)]

pub trait Trait {
    /// [dep1]
    type Item;
}

pub struct S {
    /// [dep2]
    pub x: usize,
}

extern "C" {
    /// [dep3]
    pub fn printf();
}

pub enum E {
    /// [dep4]
    A
}


