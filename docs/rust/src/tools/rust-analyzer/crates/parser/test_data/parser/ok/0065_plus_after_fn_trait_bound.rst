src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0065_plus_after_fn_trait_bound.rs
===========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f<T>() where T: Fn() -> u8 + Send {}


