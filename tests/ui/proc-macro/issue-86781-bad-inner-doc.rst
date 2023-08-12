tests/ui/proc-macro/issue-86781-bad-inner-doc.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs
// run-rustfix

#[macro_use]
extern crate test_macros;

//! Inner doc comment
//~^ ERROR expected outer doc comment
#[derive(Empty)]
pub struct Foo; //~ NOTE the inner doc comment doesn't annotate this struct

fn main() {}


