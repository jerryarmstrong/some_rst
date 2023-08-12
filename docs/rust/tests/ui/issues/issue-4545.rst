tests/ui/issues/issue-4545.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-4545.rs

// pretty-expanded FIXME #23616

extern crate issue_4545 as somelib;
pub fn main() { somelib::mk::<isize>(); }


