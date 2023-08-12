src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0046_extern_inner_attributes.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "C" {
    //! This is a doc comment
    #![doc("This is also a doc comment")]
}


