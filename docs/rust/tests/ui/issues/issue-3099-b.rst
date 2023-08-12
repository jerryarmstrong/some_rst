tests/ui/issues/issue-3099-b.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod a {}

pub mod a {} //~ ERROR the name `a` is defined multiple times

fn main() {}


