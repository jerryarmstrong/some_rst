tests/rustdoc/auto_aliases.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]

// @has auto_aliases/trait.Bar.html '//*[@data-aliases="auto_aliases::Foo"]' 'impl Bar for Foo'
pub struct Foo;

pub auto trait Bar {}


