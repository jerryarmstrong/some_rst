tests/ui/hygiene/extern-prelude-from-opaque-fail.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

macro a() {
    extern crate core as my_core;
    mod v {
        // Early resolution.
        use my_core; //~ ERROR unresolved import `my_core`
    }
    mod u {
        // Late resolution.
        fn f() { my_core::mem::drop(0); }
        //~^ ERROR failed to resolve: use of undeclared crate or module `my_core`
    }
}

a!();

mod v {
    // Early resolution.
    use my_core; //~ ERROR unresolved import `my_core`
}
mod u {
    // Late resolution.
    fn f() { my_core::mem::drop(0); }
    //~^ ERROR failed to resolve: use of undeclared crate or module `my_core`
}

fn main() {}


