tests/ui/xcrate/auxiliary/xcrate_unit_struct.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

// used by the rpass test

#[derive(Copy, Clone)]
pub struct Struct;

#[derive(Copy, Clone)]
pub enum Unit {
    UnitVariant,
    Argument(Struct)
}

#[derive(Copy, Clone)]
pub struct TupleStruct(pub usize, pub &'static str);

// used by the cfail test

#[derive(Copy, Clone)]
pub struct StructWithFields {
    foo: isize,
}

#[derive(Copy, Clone)]
pub enum EnumWithVariants {
    EnumVariant,
    EnumVariantArg(isize)
}


