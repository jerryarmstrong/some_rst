tests/ui/coherence/coherence_copy_like_err_fundamental_struct_tuple.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we are able to introduce a negative constraint that
// `MyType: !MyTrait` along with other "fundamental" wrappers.

// aux-build:coherence_copy_like_lib.rs


extern crate coherence_copy_like_lib as lib;

struct MyType { x: i32 }

trait MyTrait { fn foo() {} }

impl<T: lib::MyCopy> MyTrait for T { }

// Tuples are not fundamental.
impl MyTrait for lib::MyFundamentalStruct<(MyType,)> { }
//~^ ERROR E0119


fn main() { }


