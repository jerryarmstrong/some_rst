tests/ui/sized-borrowed-pointer.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
// Possibly-dynamic size of typaram should be cleared at pointer boundary.

// pretty-expanded FIXME #23616

fn bar<T: Sized>() { }
fn foo<T>() { bar::<&T>() }
pub fn main() { }


