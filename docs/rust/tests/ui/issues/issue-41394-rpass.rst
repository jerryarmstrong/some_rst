tests/ui/issues/issue-41394-rpass.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-41394.rs

extern crate issue_41394 as lib;

fn main() {
    assert_eq!(lib::foo() as u32, 42);
}


