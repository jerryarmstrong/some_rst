tests/rustdoc/strip-block-doc-comments-stars.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]

// The goal of this test is to ensure that it won't be generated as a list because
// block doc comments can have their lines starting with a star.

// @has foo/fn.foo.html
// @snapshot docblock - '//*[@class="toggle top-doc"]//*[@class="docblock"]'
/**
 *     a
 */
pub fn foo() {}


