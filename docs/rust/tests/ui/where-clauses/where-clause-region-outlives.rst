tests/ui/where-clauses/where-clause-region-outlives.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_variables)]
// pretty-expanded FIXME #23616

struct A<'a, 'b> where 'a : 'b { x: &'a isize, y: &'b isize }

fn main() {
    let x = 1;
    let y = 1;
    let a = A { x: &x, y: &y };
}


