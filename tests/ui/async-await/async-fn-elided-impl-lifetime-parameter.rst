tests/ui/async-await/async-fn-elided-impl-lifetime-parameter.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that `async fn` inside of an impl with `'_`
// in the header compiles correctly.
//
// Regression test for #63500.
//
// check-pass
// edition:2018

struct Foo<'a>(&'a u8);

impl Foo<'_> {
    async fn bar() {}
}

fn main() { }


