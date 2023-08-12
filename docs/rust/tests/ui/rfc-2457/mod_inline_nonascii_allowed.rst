tests/ui/rfc-2457/mod_inline_nonascii_allowed.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

mod řųśť {
    const IS_GREAT: bool = true;
}

fn main() {}


