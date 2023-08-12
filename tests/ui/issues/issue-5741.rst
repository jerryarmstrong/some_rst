tests/ui/issues/issue-5741.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616
#![allow(while_true)]
#![allow(unreachable_code)]

pub fn main() {
    return;
    while true {};
}


