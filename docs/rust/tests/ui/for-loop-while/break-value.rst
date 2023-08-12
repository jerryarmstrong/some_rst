tests/ui/for-loop-while/break-value.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unreachable_code)]
// pretty-expanded FIXME #23616

fn int_id(x: isize) -> isize { return x; }

pub fn main() { loop { int_id(break); } }


