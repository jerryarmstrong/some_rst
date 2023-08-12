tests/rustdoc/union.rs
======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has union/union.U.html
pub union U {
    // @has - //pre "pub a: u8"
    pub a: u8,
    // @has - //pre "/* private fields */"
    // @!has - //pre "b: u16"
    b: u16,
}


