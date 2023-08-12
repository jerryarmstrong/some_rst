tests/rustdoc/check-styled-link.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

pub struct Foo;

// @has foo/struct.Bar.html '//a[@href="struct.Foo.html"]' 'Foo'

/// Code-styled reference to [`Foo`].
pub struct Bar;


