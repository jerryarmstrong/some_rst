tests/ui/issues/issue-9155.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-9155.rs

// pretty-expanded FIXME #23616

extern crate issue_9155;

struct Baz;

pub fn main() {
    issue_9155::Foo::new(Baz);
}


