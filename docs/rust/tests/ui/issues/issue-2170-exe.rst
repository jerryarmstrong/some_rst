tests/ui/issues/issue-2170-exe.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-2170-lib.rs
// pretty-expanded FIXME #23616

extern crate issue_2170_lib;

pub fn main() {
   // let _ = issue_2170_lib::rsrc(2);
}


