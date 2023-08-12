shank-idl/tests/fixtures/types/valid_single_enum_shank_type.rs
==============================================================

Last edited: 2023-07-29 23:58:28

Contents:

.. code-block:: rs

    #[derive(ShankType)]
pub enum Color {
    Red(u8),
    Green(u8),
    Blue(u8),
    White,
}


