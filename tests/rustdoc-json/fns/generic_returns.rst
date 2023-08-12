tests/rustdoc-json/fns/generic_returns.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-linelength

#![feature(no_core)]
#![no_core]

// @count "$.index[*][?(@.name=='generic_returns')].inner.items[*]" 2

// @set foo = "$.index[*][?(@.name=='Foo')].id"
pub trait Foo {}

// @is "$.index[*][?(@.name=='get_foo')].inner.decl.inputs" []
// @is "$.index[*][?(@.name=='get_foo')].inner.decl.output.kind" '"impl_trait"'
// @count "$.index[*][?(@.name=='get_foo')].inner.decl.output.inner[*]" 1
// @is "$.index[*][?(@.name=='get_foo')].inner.decl.output.inner[0].trait_bound.trait.id" $foo
pub fn get_foo() -> impl Foo {
    Fooer {}
}

struct Fooer {}

impl Foo for Fooer {}


