tests/ui/functions-closures/closure_to_fn_coercion-expected-types.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// Ensure that we deduce expected argument types when a `fn()` type is expected (#41755)

fn foo(f: fn(Vec<u32>) -> usize) { }

fn main() {
    foo(|x| x.len())
}


