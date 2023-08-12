tests/rustdoc/negative-impl.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(negative_impls)]

// @matches negative_impl/struct.Alpha.html '//pre' "pub struct Alpha"
pub struct Alpha;
// @matches negative_impl/struct.Bravo.html '//pre' "pub struct Bravo<B>"
pub struct Bravo<B>(B);

// @matches negative_impl/struct.Alpha.html '//*[@class="impl has-srclink"]//h3[@class="code-header"]' \
// "impl !Send for Alpha"
impl !Send for Alpha {}

// @matches negative_impl/struct.Bravo.html '//*[@class="impl has-srclink"]//h3[@class="code-header"]' "\
// impl<B> !Send for Bravo<B>"
impl<B> !Send for Bravo<B> {}


