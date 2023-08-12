src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0007_type_param_bounds.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S<T: 'a + ?Sized + (Copy) + ~const Drop>;


