src/tools/rustfmt/tests/target/issue-3717.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    {
        #[rustfmt::skip]
        let _ = 
        [1];
    }
}


