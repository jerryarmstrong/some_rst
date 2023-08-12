src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0050_async_block_as_argument.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: impl std::future::Future<Output = i32>) {}

fn main() {
    foo(async move { 12 })
}


