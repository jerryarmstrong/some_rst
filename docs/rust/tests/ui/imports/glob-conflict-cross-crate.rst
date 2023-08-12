tests/ui/imports/glob-conflict-cross-crate.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:glob-conflict.rs

extern crate glob_conflict;

fn main() {
    glob_conflict::f(); //~ ERROR cannot find function `f` in crate `glob_conflict`
    glob_conflict::glob::f(); //~ ERROR cannot find function `f` in module `glob_conflict::glob`
}


