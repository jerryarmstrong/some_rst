tests/ui/inline-disallow-on-variant.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    #[inline]
    //~^ ERROR attribute should be applied
    Variant,
}

fn main() {}


