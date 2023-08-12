tests/ui/binding/match-bot-2.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unreachable_code)]
// n.b. This was only ever failing with optimization disabled.

fn a() -> isize { match return 1 { 2 => 3, _ => panic!() } }
pub fn main() { a(); }


