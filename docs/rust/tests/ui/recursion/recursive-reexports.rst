tests/ui/recursion/recursive-reexports.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:recursive_reexports.rs

extern crate recursive_reexports;

fn f() -> recursive_reexports::S {} //~ ERROR cannot find type `S` in crate `recursive_reexports`

fn main() {}


