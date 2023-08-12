tests/rustdoc/implementor-stable-version.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![stable(feature = "bar", since = "OLD 1.0")]
#![crate_name = "foo"]

#![feature(staged_api)]

#[stable(feature = "bar", since = "OLD 1.0")]
pub trait Bar {}

#[stable(feature = "baz", since = "OLD 1.0")]
pub trait Baz {}

#[stable(feature = "baz", since = "OLD 1.0")]
pub struct Foo;

// @has foo/trait.Bar.html '//div[@id="implementors-list"]//span[@class="since"]' 'NEW 2.0'
#[stable(feature = "foobar", since = "NEW 2.0")]
impl Bar for Foo {}

// @!has foo/trait.Baz.html '//div[@id="implementors-list"]//span[@class="since"]' 'OLD 1.0'
#[stable(feature = "foobaz", since = "OLD 1.0")]
impl Baz for Foo {}


