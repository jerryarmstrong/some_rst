src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0026_tuple_pat_fields.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    let S() = ();
    let S(_) = ();
    let S(_,) = ();
    let S(_, .. , x) = ();
    let S(| a) = ();
}


