tests/ui/inference/newlambdas-ret-infer.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// Test that the lambda kind is inferred correctly as a return
// expression

// pretty-expanded FIXME #23616

fn unique() -> Box<dyn FnMut()+'static> { return Box::new(|| ()); }

pub fn main() {
}


