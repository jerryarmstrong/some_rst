tests/rustdoc-json/enums/struct_field_hidden.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Foo {
    Variant {
        #[doc(hidden)]
        a: i32,
        // @set b = "$.index[*][?(@.name=='b')].id"
        b: i32,
        #[doc(hidden)]
        x: i32,
        // @set y = "$.index[*][?(@.name=='y')].id"
        y: i32,
    },
    // @is "$.index[*][?(@.name=='Variant')].inner.kind.struct.fields_stripped" true
    // @is "$.index[*][?(@.name=='Variant')].inner.kind.struct.fields[0]" $b
    // @is "$.index[*][?(@.name=='Variant')].inner.kind.struct.fields[1]" $y
    // @count "$.index[*][?(@.name=='Variant')].inner.kind.struct.fields[*]" 2
}


