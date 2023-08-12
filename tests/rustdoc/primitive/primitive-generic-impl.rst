tests/rustdoc/primitive/primitive-generic-impl.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustdoc_internals)]
#![crate_name = "foo"]

// @has foo/primitive.i32.html '//*[@id="impl-ToString-for-i32"]//h3[@class="code-header"]' 'impl<T> ToString for T'

#[doc(primitive = "i32")]
/// Some useless docs, wouhou!
mod i32 {}


