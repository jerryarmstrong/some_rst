tests/ui/issues/issue-2380-b.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:issue-2380.rs

// pretty-expanded FIXME #23616

extern crate a;

pub fn main() {
    a::f::<()>();
}


