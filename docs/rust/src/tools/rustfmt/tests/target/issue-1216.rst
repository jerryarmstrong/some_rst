src/tools/rustfmt/tests/target/issue-1216.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-normalize_comments: true
enum E {
    A, //* I am not a block comment (caused panic)
    B,
}


