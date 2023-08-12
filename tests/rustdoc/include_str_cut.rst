tests/rustdoc/include_str_cut.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]
#![no_std]

// @has 'foo/fn.foo.html'
// @has - '//*[@class="docblock"]' 'inc2 x'
#[doc = include_str!("short-line.md")]
pub fn foo() {}


