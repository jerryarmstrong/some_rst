tests/rustdoc-json/impls/blanket_with_local.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for the ICE in rust/83718
// A blanket impl plus a local type together shouldn't result in mismatched ID issues

// @has "$.index[*][?(@.name=='Load')]"
pub trait Load {
    // @has "$.index[*][?(@.name=='load')]"
    fn load() {}
    // @has "$.index[*][?(@.name=='write')]"
    fn write(self) {}
}

impl<P> Load for P {
    fn load() {}
    fn write(self) {}
}

// @has "$.index[*][?(@.name=='Wrapper')]"
pub struct Wrapper {}


