tests/rustdoc/issue-47197-blank-line-in-doc-block.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // @has issue_47197_blank_line_in_doc_block/fn.whose_woods_these_are_i_think_i_know.html

/**
* snow

* ice
*/
pub fn whose_woods_these_are_i_think_i_know() {}


