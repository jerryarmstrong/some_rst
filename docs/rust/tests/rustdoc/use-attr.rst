tests/rustdoc/use-attr.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// ICE when rustdoc encountered a use statement of a non-macro attribute (see #58054)

// @has use_attr/index.html
// @has - '//code' 'pub use proc_macro_attribute'
pub use proc_macro_attribute;
use proc_macro_derive;


