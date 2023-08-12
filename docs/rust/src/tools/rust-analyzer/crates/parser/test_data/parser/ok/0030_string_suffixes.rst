src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0030_string_suffixes.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = 'c'u32;
    let _ = "string"invalid;
    let _ = b'b'_suff;
    let _ = b"bs"invalid;
}


