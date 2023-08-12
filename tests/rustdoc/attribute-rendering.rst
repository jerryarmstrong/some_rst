tests/rustdoc/attribute-rendering.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// @has 'foo/fn.f.html'
// @has - //*[@'class="item-decl"]' '#[export_name = "f"] pub fn f()'
#[export_name = "\
f"]
pub fn f() {}


