tests/ui/regions/regions-link-fn-args.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that region inference correctly links up the regions when a
// `ref` borrow occurs inside a fn argument.

// pretty-expanded FIXME #23616

#![allow(dead_code)]

fn with<'a, F>(_: F) where F: FnOnce(&'a Vec<isize>) -> &'a Vec<isize> { }

fn foo() {
    with(|&ref ints| ints);
}

fn main() { }


