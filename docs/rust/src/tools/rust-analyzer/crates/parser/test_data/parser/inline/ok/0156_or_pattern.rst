src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0156_or_pattern.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match () {
        (_ | _) => (),
        &(_ | _) => (),
        (_ | _,) => (),
        [_ | _,] => (),
    }
}


