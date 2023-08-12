tests/ui/attributes/unnamed-field-attributes-vis.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Unnamed fields don't lose their visibility due to non-builtin attributes on them.

// check-pass

mod m {
    pub struct S(#[rustfmt::skip] pub u8);
}

fn main() {
    m::S(0);
}


