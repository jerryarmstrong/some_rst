src/tools/rust-analyzer/crates/parser/test_data/parser/err/0032_match_arms_inner_attrs.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    match () {
        _ => (),
        #![doc("Not allowed here")]
        _ => (),
    }

    match () {
        _ => (),
        _ => (),
        #![doc("Nor here")]
    }

    match () {
        #[cfg(test)]
        #![doc("Nor here")]
        _ => (),
        _ => (),
    }
}


