src/tools/rustfmt/tests/target/issue-2446.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Issue2446 {
    V {
        f: u8, // x
    },
}

enum Issue2446TrailingCommentsOnly {
    V { f: u8 /* */ },
}


