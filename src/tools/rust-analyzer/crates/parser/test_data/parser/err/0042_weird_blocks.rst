src/tools/rust-analyzer/crates/parser/test_data/parser/err/0042_weird_blocks.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    { unsafe 92 }
    { async 92 }
    { try 92 }
    { 'label: 92 }
}


