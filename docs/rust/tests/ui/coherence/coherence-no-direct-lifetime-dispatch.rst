tests/ui/coherence/coherence-no-direct-lifetime-dispatch.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that you cannot *directly* dispatch on lifetime requirements

trait MyTrait { fn foo() {} }

impl<T> MyTrait for T {}
impl<T: 'static> MyTrait for T {}
//~^ ERROR E0119

fn main() {}


