tests/ui/consts/closure-structural-match-issue-90013.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue 90013.
// check-pass
#![feature(inline_const)]

fn main() {
    const { || {} };
}


