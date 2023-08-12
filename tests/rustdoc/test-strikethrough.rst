tests/rustdoc/test-strikethrough.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has foo/fn.f.html
// @has - //del "Y"
/// ~~Y~~
pub fn f() {}


