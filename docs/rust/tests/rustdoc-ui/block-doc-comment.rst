tests/rustdoc-ui/block-doc-comment.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags:--test
// normalize-stdout-test "finished in \d+\.\d+s" -> "finished in $$TIME"

// This test ensures that no code block is detected in the doc comments.

pub mod Wormhole {
    /** # Returns
     *
     */
    pub fn foofoo() {}
    /**
     * # Returns
     *
     */
    pub fn barbar() {}
}


