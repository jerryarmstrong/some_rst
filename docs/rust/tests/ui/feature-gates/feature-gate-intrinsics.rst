tests/ui/feature-gates/feature-gate-intrinsics.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "rust-intrinsic" {   //~ ERROR intrinsics are subject to change
    fn bar(); //~ ERROR unrecognized intrinsic function: `bar`
}

extern "rust-intrinsic" fn baz() {} //~ ERROR intrinsics are subject to change
//~^ ERROR intrinsic must be in

fn main() {}


