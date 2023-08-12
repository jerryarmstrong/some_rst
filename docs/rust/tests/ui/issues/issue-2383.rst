tests/ui/issues/issue-2383.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::collections::VecDeque;

pub fn main() {
    let mut q = VecDeque::new();
    q.push_front(10);
}


