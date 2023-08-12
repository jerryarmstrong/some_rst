src/tools/rustfmt/tests/target/issue_4963.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod test {
    extern "C" {
        fn test();
    }
}

extern "C" {
    fn test();
}


