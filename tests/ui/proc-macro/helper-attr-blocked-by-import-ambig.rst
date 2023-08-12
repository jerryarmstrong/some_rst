tests/ui/proc-macro/helper-attr-blocked-by-import-ambig.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:test-macros.rs

#[macro_use(Empty)]
extern crate test_macros;
use test_macros::empty_attr as empty_helper;

#[empty_helper] //~ ERROR `empty_helper` is ambiguous
                //~| WARN derive helper attribute is used before it is introduced
                //~| WARN this was previously accepted
#[derive(Empty)]
struct S;

fn main() {}


