tests/rustdoc/fn-bound.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #100143

use std::iter::Peekable;

pub struct Span<F: Fn(&i32)> {
    inner: Peekable<ConditionalIterator<F>>,
}

pub struct ConditionalIterator<F> {
    f: F,
}


// @has 'fn_bound/struct.ConditionalIterator.html' '//h3[@class="code-header"]' 'impl<F: Fn(&i32)> Iterator for ConditionalIterator<F>'
impl<F: Fn(&i32)> Iterator for ConditionalIterator<F> {
    type Item = ();

    fn next(&mut self) -> Option<Self::Item> {
        todo!()
    }
}


