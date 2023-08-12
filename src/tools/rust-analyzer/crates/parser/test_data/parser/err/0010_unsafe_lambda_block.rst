src/tools/rust-analyzer/crates/parser/test_data/parser/err/0010_unsafe_lambda_block.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    || -> () unsafe { () };
}


