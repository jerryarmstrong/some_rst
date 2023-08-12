tests/ui/issues/issue-3878.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![allow(path_statements)]

pub fn main() {
    let y: Box<_> = Box::new(1);
    y;
}


