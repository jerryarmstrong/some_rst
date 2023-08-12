tests/ui/attributes/unnamed-field-attributes.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct S(
    #[rustfmt::skip] u8,
    u16,
    #[rustfmt::skip] u32,
);

fn main() {}


