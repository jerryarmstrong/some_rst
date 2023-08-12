tests/ui/proc-macro/doc-comment-preserved.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z span-debug
// aux-build:test-macros.rs

#![no_std] // Don't load unnecessary hygiene information from std
extern crate std;

#[macro_use]
extern crate test_macros;

print_bang! {

/**
*******
* DOC *
* DOC *
* DOC *
*******
*/
pub struct S;

}

fn main() {}


