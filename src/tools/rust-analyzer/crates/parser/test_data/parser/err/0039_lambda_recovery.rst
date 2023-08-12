src/tools/rust-analyzer/crates/parser/test_data/parser/err/0039_lambda_recovery.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> i32 {
    [1, 2, 3].iter()
        .map(|it|)
        .max::<i32>();
}


