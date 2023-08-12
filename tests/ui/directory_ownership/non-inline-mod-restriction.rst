tests/ui/directory_ownership/non-inline-mod-restriction.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that non-inline modules are not allowed inside blocks.

fn main() {
    mod foo; //~ ERROR cannot declare a non-inline module inside a block
}


