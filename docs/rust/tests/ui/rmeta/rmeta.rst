tests/ui/rmeta/rmeta.rs
=======================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
// compile-flags: --emit=metadata

// Check that building a metadata crate finds an error.

fn main() {
    let _ = Foo; //~ ERROR cannot find value `Foo` in this scope
}


