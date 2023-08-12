tests/ui/enum-discriminant/arbitrary_enum_discriminant-no-repr.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

enum Enum {
//~^ ERROR `#[repr(inttype)]` must be specified
  Unit = 1,
  Tuple() = 2,
  Struct{} = 3,
}


