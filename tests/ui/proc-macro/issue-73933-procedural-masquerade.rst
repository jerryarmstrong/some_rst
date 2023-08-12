tests/ui/proc-macro/issue-73933-procedural-masquerade.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs
// check-pass

#[macro_use]
extern crate test_macros;

#[derive(Print)]
enum ProceduralMasqueradeDummyType {
    Input
}

fn main() {}


