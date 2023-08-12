src/tools/rustfmt/tests/target/issue-2995.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn issue_2995() {
    // '\u{2028}' is inserted in the code below.

    [0, 1];
    [0, /* */ 1];
    [0, 1];
}


