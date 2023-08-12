tests/pretty/issue-12590-a.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact
// pretty-compare-only

// The next line should not be expanded

#[path = "issue-12590-b.rs"]
mod issue_12590_b;

fn main() {}


