tests/pretty/do1.rs
===================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

fn f<F>(f: F) where F: Fn(isize) { f(10) }

fn main() { f(|i| { assert_eq!(i, 10) }) }


