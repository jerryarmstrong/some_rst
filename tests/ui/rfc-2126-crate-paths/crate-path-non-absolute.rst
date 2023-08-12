tests/ui/rfc-2126-crate-paths/crate-path-non-absolute.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;

pub mod m {
    fn f() {
        let s = ::m::crate::S; //~ ERROR failed to resolve
        let s1 = ::crate::S; //~ ERROR failed to resolve
        let s2 = crate::S; // no error
    }
}

fn main() {}


