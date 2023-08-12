tests/ui/coherence/coherence_local_err_struct.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are able to introduce a negative constraint that
// `MyType: !MyTrait` along with other "fundamental" wrappers.

// aux-build:coherence_copy_like_lib.rs
#![allow(dead_code)]

extern crate coherence_copy_like_lib as lib;

struct MyType { x: i32 }

// These are all legal because they are all fundamental types:

// MyStruct is not fundamental.
impl lib::MyCopy for lib::MyStruct<MyType> { }
//~^ ERROR E0117


fn main() { }


