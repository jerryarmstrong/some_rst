tests/rustdoc-ui/intra-doc/macro-rules.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(rustdoc::private_intra_doc_links)]

macro_rules! foo {
    () => {};
}

/// [foo!]
pub fn baz() {}

#[macro_use]
mod macros {
    macro_rules! escaping {
        () => {};
    }
}

pub mod inner {
    /// [foo!]
    /// [escaping]
    pub fn baz() {
        foo!();
    }
}


