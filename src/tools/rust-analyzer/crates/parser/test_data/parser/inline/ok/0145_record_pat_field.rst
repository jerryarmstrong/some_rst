src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0145_record_pat_field.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let S { 0: 1 } = ();
    let S { x: 1 } = ();
    let S { #[cfg(any())] x: 1 } = ();
}


