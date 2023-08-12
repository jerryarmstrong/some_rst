tests/ui/hygiene/stdlib-prelude-from-opaque-late.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![feature(decl_macro)]

macro mac() {
    mod m {
        fn f() {
            std::mem::drop(0); // OK (extern prelude)
            drop(0); // OK (stdlib prelude)
        }
    }
}

mac!();

fn main() {}


