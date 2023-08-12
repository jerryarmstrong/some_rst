tests/pretty/struct-pattern.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact
// pretty-compare-only
// Testing that shorthand struct patterns are preserved

fn main() { let Foo { a, ref b, mut c, x: y, z: z } = foo; }


