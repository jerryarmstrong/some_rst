tests/rustdoc/cap-lints.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail a normal compile due to non_camel_case_types,
// It should pass a doc-compile as it only needs to type-check and
// therefore should not concern itself with the lints.
#[deny(warnings)]

// @has cap_lints/struct.Foo.html //* 'Foo'
pub struct Foo {
    field: i32,
}


