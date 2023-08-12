tests/ui/for-loop-while/while-flow-graph.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


// pretty-expanded FIXME #23616

pub fn main() { let x: isize = 10; while x == 10 && x == 11 { let _y = 0xf00_usize; } }


