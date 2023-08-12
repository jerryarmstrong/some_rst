tests/ui/rfc-2008-non-exhaustive/improper_ctypes/auxiliary/types.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[non_exhaustive]
#[repr(C)]
pub enum NonExhaustiveEnum {
    Unit,
    Tuple(u32),
    Struct { field: u32 }
}

#[non_exhaustive]
#[repr(C)]
pub struct NormalStruct {
    pub first_field: u16,
    pub second_field: u16,
}

#[non_exhaustive]
#[repr(C)]
pub struct UnitStruct;

#[non_exhaustive]
#[repr(C)]
pub struct TupleStruct (pub u16, pub u16);

#[repr(C)]
pub enum NonExhaustiveVariants {
    #[non_exhaustive] Unit,
    #[non_exhaustive] Tuple(u32),
    #[non_exhaustive] Struct { field: u32 }
}


