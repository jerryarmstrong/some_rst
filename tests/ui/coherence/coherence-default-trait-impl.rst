tests/ui/coherence/coherence-default-trait-impl.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]
#![feature(negative_impls)]

auto trait MySafeTrait {}

struct Foo;

unsafe impl MySafeTrait for Foo {}
//~^ ERROR E0199

unsafe auto trait MyUnsafeTrait {}

impl MyUnsafeTrait for Foo {}
//~^ ERROR E0200

fn main() {}


