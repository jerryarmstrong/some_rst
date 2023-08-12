tests/pretty/fn-types.rs
========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // pp-exact

fn from_foreign_fn(_x: fn()) {}
fn from_stack_closure<F>(_x: F) where F: Fn() {}
fn main() {}


