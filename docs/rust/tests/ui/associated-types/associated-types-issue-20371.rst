tests/ui/associated-types/associated-types-issue-20371.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that we are able to have an impl that defines an associated type
// before the actual trait.

// pretty-expanded FIXME #23616

impl X for f64 { type Y = isize; }
trait X { type Y; }
fn main() {}


