tests/rustdoc/intra-doc/cross-crate/auxiliary/submodule-outer.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "bar"]
#![deny(rustdoc::broken_intra_doc_links)]

pub trait Foo {
    /// [`Bar`] [`Baz`]
    fn foo();
}

pub trait Bar {
}

pub trait Baz {
}


