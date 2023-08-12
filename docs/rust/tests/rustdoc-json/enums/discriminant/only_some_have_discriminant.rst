tests/rustdoc-json/enums/discriminant/only_some_have_discriminant.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum Foo {
    // @is "$.index[*][?(@.name=='Has')].inner.discriminant" '{"expr":"0", "value":"0"}'
    Has = 0,
    // @is "$.index[*][?(@.name=='Doesnt')].inner.discriminant" null
    Doesnt,
    // @is "$.index[*][?(@.name=='AlsoDoesnt')].inner.discriminant" null
    AlsoDoesnt,
    // @is "$.index[*][?(@.name=='AlsoHas')].inner.discriminant" '{"expr":"44", "value":"44"}'
    AlsoHas = 44,
}


