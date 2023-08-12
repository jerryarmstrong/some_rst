tests/rustdoc/negative-impl-sidebar.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]
#![crate_name = "foo"]

pub struct Foo;

// @has foo/struct.Foo.html
// @has - '//div[@class="sidebar-elems"]//h3/a[@href="#trait-implementations"]' 'Trait Implementations'
// @has - '//*[@class="sidebar-elems"]//section//a' '!Sync'
impl !Sync for Foo {}


