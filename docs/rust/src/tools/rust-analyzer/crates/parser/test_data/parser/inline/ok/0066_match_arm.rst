src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0066_match_arm.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        _ => (),
        _ if Test > Test{field: 0} => (),
        X | Y if Z => (),
        | X | Y if Z => (),
        | X => (),
    };
}


