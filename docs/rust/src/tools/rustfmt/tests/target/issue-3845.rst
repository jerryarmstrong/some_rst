src/tools/rustfmt/tests/target/issue-3845.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    || {
        #[allow(deprecated)]
        {
            u8::max_value()
        }
    };
}


