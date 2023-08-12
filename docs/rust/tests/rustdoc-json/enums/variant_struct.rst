tests/rustdoc-json/enums/variant_struct.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @is "$.index[*][?(@.name=='EnumStruct')].visibility" \"public\"
// @is "$.index[*][?(@.name=='EnumStruct')].kind" \"enum\"
pub enum EnumStruct {
    // @is "$.index[*][?(@.name=='x')].kind" \"struct_field\"
    // @set x = "$.index[*][?(@.name=='x')].id"
    // @is "$.index[*][?(@.name=='y')].kind" \"struct_field\"
    // @set y = "$.index[*][?(@.name=='y')].id"
    // @ismany "$.index[*][?(@.name=='VariantS')].inner.kind.struct.fields[*]" $x $y
    VariantS { x: u32, y: String },
}


