tests/pretty/issue-12590-c.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pretty-compare-only
// pretty-mode:expanded
// pp-exact:issue-12590-c.pp

// The next line should be expanded

#[path = "issue-12590-b.rs"]
mod issue_12590_b;

fn main() {}


