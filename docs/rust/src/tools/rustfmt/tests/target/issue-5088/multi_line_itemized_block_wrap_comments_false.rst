src/tools/rustfmt/tests/target/issue-5088/multi_line_itemized_block_wrap_comments_false.rs
==========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: false

// - some itemized block 1
// - some itemized block 2

// * some itemized block 3
// * some itemized block 4

/*
 * - some itemized block 5
 * - some itemized block 6
 */

/*
 * * some itemized block 7
 * * some itemized block 8
 */


