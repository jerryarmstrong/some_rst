tests/ui/attributes/unnamed-field-attributes-dup.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Duplicate non-builtin attributes can be used on unnamed fields.

// check-pass

struct S (
    #[rustfmt::skip]
    #[rustfmt::skip]
    u8
);

fn main() {}


