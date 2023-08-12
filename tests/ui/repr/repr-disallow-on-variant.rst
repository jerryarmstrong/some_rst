tests/ui/repr/repr-disallow-on-variant.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Test;

enum Foo {
    #[repr(u8)]
    //~^ ERROR attribute should be applied to an enum
    Variant,
}

fn main() {}


