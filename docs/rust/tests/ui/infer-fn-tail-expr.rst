tests/ui/infer-fn-tail-expr.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// issue #680


// pretty-expanded FIXME #23616

fn f() -> Vec<isize> { Vec::new() }

pub fn main() { }


