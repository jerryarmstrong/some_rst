tests/rustdoc/empty-section.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

#![feature(negative_impls)]

pub struct Foo;

// @has foo/struct.Foo.html
// @!hasraw - 'Auto Trait Implementations'
impl !Send for Foo {}
impl !Sync for Foo {}
impl !std::marker::Unpin for Foo {}
impl !std::panic::RefUnwindSafe for Foo {}
impl !std::panic::UnwindSafe for Foo {}


