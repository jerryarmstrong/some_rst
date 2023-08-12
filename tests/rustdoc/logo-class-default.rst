tests/rustdoc/logo-class-default.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Note: this test is paired with logo-class.rs.
// @has logo_class_default/struct.SomeStruct.html '//*[@class="logo-container"]/img[@class="rust-logo"]' ''
// @has src/logo_class_default/logo-class-default.rs.html '//*[@class="sub-logo-container"]/img[@class="rust-logo"]' ''
pub struct SomeStruct;


