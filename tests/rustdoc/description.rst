tests/rustdoc/description.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]
//! # Description test crate
//!
//! This is the contents of the test crate docstring.
//! It should not show up in the description.

// @has 'foo/index.html' '//meta[@name="description"]/@content' \
//   'Description test crate'
// @!has - '//meta[@name="description"]/@content' 'should not show up'

// @has 'foo/foo_mod/index.html' '//meta[@name="description"]/@content' \
//   'First paragraph description.'
// @!has - '//meta[@name="description"]/@content' 'Second paragraph'
/// First paragraph description.
///
/// Second paragraph should not show up.
pub mod foo_mod {
    pub struct __Thing {}
}

// @has 'foo/fn.foo_fn.html' '//meta[@name="description"]/@content' \
//   'Only paragraph.'
/// Only paragraph.
pub fn foo_fn() {}


