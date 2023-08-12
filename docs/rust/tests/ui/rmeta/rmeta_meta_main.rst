tests/ui/rmeta/rmeta_meta_main.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --emit=metadata
// aux-build:rmeta-meta.rs
// no-prefer-dynamic

// Check that building a metadata crate finds an error with a dependent,
// metadata-only crate.


extern crate rmeta_meta;
use rmeta_meta::Foo;

fn main() {
    let _ = Foo { field2: 42 }; //~ ERROR struct `Foo` has no field named `field2`
}


