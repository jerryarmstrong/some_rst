tests/ui/issues/issue-7178.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-7178.rs

// pretty-expanded FIXME #23616

extern crate issue_7178 as cross_crate_self;

pub fn main() {
    let _ = cross_crate_self::Foo::new(&1);
}


