src/tools/rust-analyzer/crates/parser/test_data/parser/err/0034_bad_box_pattern.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let ref box i = ();
    let mut box i = ();
    let ref mut box i = ();
}



