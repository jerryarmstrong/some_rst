src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0143_box_pat.rs
================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let box i = ();
    let box Outer { box i, j: box Inner(box &x) } = ();
    let box ref mut i = ();
}


