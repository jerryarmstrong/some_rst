tests/ui/span/pub-struct-field.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #26083 and #35435
// Test that span for public struct fields start at `pub`

struct Foo {
    bar: u8,
    pub bar: u8, //~ ERROR is already declared
    pub(crate) bar: u8, //~ ERROR is already declared
}

fn main() {}


