tests/ui/lint/issue-90614-accept-allow-text-direction-codepoint-in-comment-lint.rs
==================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Allowing the code lint should work without warning and
// the text flow char in the comment should be ignored.

#![allow(text_direction_codepoint_in_comment)]

fn main() {
    // U+2066 LEFT-TO-RIGHT ISOLATE follows:⁦⁦
}


