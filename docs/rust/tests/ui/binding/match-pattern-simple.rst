tests/ui/binding/match-pattern-simple.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]


// pretty-expanded FIXME #23616

fn altsimple(f: isize) { match f { _x => () } }

pub fn main() { }


