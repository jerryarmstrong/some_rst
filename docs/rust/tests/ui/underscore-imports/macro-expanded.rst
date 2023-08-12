tests/ui/underscore-imports/macro-expanded.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that macro expanded underscore imports behave as expected

// check-pass

#![feature(decl_macro, rustc_attrs)]

mod x {
    pub use std::ops::Not as _;
}

macro m() {
    mod w {
        mod y {
            pub use std::ops::Deref as _;
        }
        use crate::x::*;
        use self::y::*;
        use std::ops::DerefMut as _;
        fn f() {
            false.not();
            (&()).deref();
            (&mut ()).deref_mut();
        }
    }
}

#[rustc_macro_transparency = "transparent"]
macro n() {
    mod z {
        pub use std::ops::Deref as _;
    }
    use crate::x::*;
    use crate::z::*;
    use std::ops::DerefMut as _;
    fn f() {
        false.not();
        (&()).deref();
        (&mut ()).deref_mut();
    }
}

m!();
n!();

fn main() {}


