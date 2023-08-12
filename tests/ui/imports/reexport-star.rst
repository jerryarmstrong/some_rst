tests/ui/imports/reexport-star.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

mod a {
    pub fn f() {}
    pub fn g() {}
}

mod b {
    pub use a::*;
}

pub fn main() {
    b::f();
    b::g();
}


