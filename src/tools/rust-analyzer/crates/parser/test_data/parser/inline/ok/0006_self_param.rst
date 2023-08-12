src/tools/rust-analyzer/crates/parser/test_data/parser/inline/ok/0006_self_param.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    impl S {
    fn a(self) {}
    fn b(&self,) {}
    fn c(&'a self,) {}
    fn d(&'a mut self, x: i32) {}
    fn e(mut self) {}
}


