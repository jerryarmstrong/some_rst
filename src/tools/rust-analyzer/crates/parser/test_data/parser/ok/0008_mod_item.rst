src/tools/rust-analyzer/crates/parser/test_data/parser/ok/0008_mod_item.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod c {
    fn foo() {
    }
    struct S {}
}

mod d {
    #![attr]
    mod e;
    mod f {
    }
}


