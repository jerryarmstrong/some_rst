tests/ui/where-clauses/where-clauses-lifetimes.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_mut)]
#![allow(unused_variables)]
// pretty-expanded FIXME #23616

fn foo<'a, I>(mut it: I) where I: Iterator<Item=&'a isize> {}

fn main() {
    foo([1, 2].iter());
}


