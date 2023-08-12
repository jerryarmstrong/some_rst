tests/ui/issues/issue-5950.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// pretty-expanded FIXME #23616

pub use local as local_alias;

pub mod local { }

pub fn main() {}


