tests/ui/feature-gates/issue-43106-gating-of-unstable.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Testing gating of `#[unstable]` in "weird" places.
//
// This file sits on its own because these signal errors, making
// this test incompatible with the "warnings only" nature of
// issue-43106-gating-of-builtin-attrs.rs

#![unstable()]
//~^ ERROR stability attributes may not be used outside of the standard library

#[unstable()]
//~^ ERROR stability attributes may not be used outside of the standard library
mod unstable {
    mod inner {
        #![unstable()]
        //~^ ERROR stability attributes may not be used outside of the standard library
    }

    #[unstable()]
    //~^ ERROR stability attributes may not be used outside of the standard library
    fn f() {}

    #[unstable()]
    //~^ ERROR stability attributes may not be used outside of the standard library
    struct S;

    #[unstable()]
    //~^ ERROR stability attributes may not be used outside of the standard library
    type T = S;

    #[unstable()]
    //~^ ERROR stability attributes may not be used outside of the standard library
    impl S {}
}

fn main() {}


