tests/ui/underscore-lifetime/underscore-outlives-bounds.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test to check that `'b: '_` gets an error, because it's
// basically useless.
//
// #54902

trait Foo<'a> {}
impl<'b: '_> Foo<'b> for i32 {} //~ ERROR `'_` cannot be used here
fn main() { }


