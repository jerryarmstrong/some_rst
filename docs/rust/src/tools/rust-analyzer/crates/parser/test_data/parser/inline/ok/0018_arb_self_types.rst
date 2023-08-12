src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0018_arb_self_types.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl S {
    fn a(self: &Self) {}
    fn b(mut self: Box<Self>) {}
}


