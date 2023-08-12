src/tools/rust-analyzer/crates/syntax/test_data/parser/validation/0031_block_inner_attrs.rs
===========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn block() {
    let inner = {
        #![doc("Inner attributes not allowed here")]
        //! Nor are ModuleDoc comments
    };
    if true {
        #![doc("Nor here")]
        #![doc("We error on each attr")]
        //! Nor are ModuleDoc comments
    }
    while true {
        #![doc("Nor here")]
        //! Nor are ModuleDoc comments
    }
}


