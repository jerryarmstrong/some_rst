src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0055_literal_pattern.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match () {
        -1 => (),
        92 => (),
        'c' => (),
        "hello" => (),
    }
}


