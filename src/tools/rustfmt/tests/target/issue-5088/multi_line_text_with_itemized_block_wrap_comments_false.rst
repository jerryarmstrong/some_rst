src/tools/rustfmt/tests/target/issue-5088/multi_line_text_with_itemized_block_wrap_comments_false.rs
====================================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-wrap_comments: false

// Some text
// - some itemized block 1
// - some itemized block 2
// Some more text
// - some itemized block 3
// - some itemized block 4
// Even more text

// Some text
// * some itemized block 5
// * some itemized block 6
// Some more text
// * some itemized block 7
// * some itemized block 8
// Even more text

/*
 * Some text
 * - some itemized block 9
 * - some itemized block 10
 * Some more text
 * - some itemized block 11
 * - some itemized block 12
 * Even more text
 */

/*
 * Some text
 * * some itemized block 13
 * * some itemized block 14
 * Some more text
 * * some itemized block 15
 * * some itemized block 16
 * Even more text
 */


