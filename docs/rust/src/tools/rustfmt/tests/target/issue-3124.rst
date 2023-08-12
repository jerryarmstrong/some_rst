src/tools/rustfmt/tests/target/issue-3124.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub fn fail1() {
    // Some comment.
    /**///
}

pub fn fail2() {
    // Some comment.
    /**/
}

pub fn fail3() {
    // Some comment.
    //
}


