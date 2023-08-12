tests/ui/issues/issue-2472.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-2472-b.rs

// pretty-expanded FIXME #23616

extern crate issue_2472_b;

use issue_2472_b::{S, T};

pub fn main() {
    let s = S(());
    s.foo();
    s.bar();
}


