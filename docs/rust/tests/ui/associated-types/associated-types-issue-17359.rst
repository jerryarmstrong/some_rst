tests/ui/associated-types/associated-types-issue-17359.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we do not ICE when an impl is missing an associated type (and that we report
// a useful error, of course).

trait Trait {
    type Type;
}

impl Trait for isize {}  //~ ERROR missing: `Type`

fn main() {}


