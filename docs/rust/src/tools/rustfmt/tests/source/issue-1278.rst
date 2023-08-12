src/tools/rustfmt/tests/source/issue-1278.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-indent_style = "block"

#![feature(pub_restricted)]

mod inner_mode {
    pub(super) fn func_name(abc: i32) -> i32 {
        abc
    }
}


