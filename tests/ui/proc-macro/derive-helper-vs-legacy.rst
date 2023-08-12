tests/ui/proc-macro/derive-helper-vs-legacy.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

#[derive(Empty)]
#[empty_helper] // OK, this is both derive helper and legacy derive helper
#[derive(Empty)]
struct S;

fn main() {}


