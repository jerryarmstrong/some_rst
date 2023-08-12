tests/ui/coherence/coherence_local.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are able to introduce a negative constraint that
// `MyType: !MyTrait` along with other "fundamental" wrappers.

// check-pass
// aux-build:coherence_copy_like_lib.rs

extern crate coherence_copy_like_lib as lib;

struct MyType { x: i32 }

// These are all legal because they are all fundamental types:

impl lib::MyCopy for MyType { }
impl<'a> lib::MyCopy for &'a MyType { }
impl<'a> lib::MyCopy for &'a Box<MyType> { }
impl lib::MyCopy for Box<MyType> { }
impl lib::MyCopy for lib::MyFundamentalStruct<MyType> { }
impl lib::MyCopy for lib::MyFundamentalStruct<Box<MyType>> { }

fn main() {}


