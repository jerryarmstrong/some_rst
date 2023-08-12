src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0048_path_type_with_bounds.rs
==============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> Box<T + 'f> {}
fn foo() -> Box<dyn T + 'f> {}


