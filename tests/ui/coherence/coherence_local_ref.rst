tests/ui/coherence/coherence_local_ref.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are able to introduce a negative constraint that
// `MyType: !MyTrait` along with other "fundamental" wrappers.

// check-pass
// aux-build:coherence_copy_like_lib.rs

extern crate coherence_copy_like_lib as lib;

struct MyType { x: i32 }

// naturally, legal
impl lib::MyCopy for MyType { }

fn main() { }


