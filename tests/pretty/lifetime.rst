tests/pretty/lifetime.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

fn f1<'a, 'b, 'c>(_x: &'a u32, _y: &'b u32, _z: &'c u32) where 'c: 'a + 'b {}

fn main() {}


