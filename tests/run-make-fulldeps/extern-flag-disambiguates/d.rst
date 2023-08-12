tests/run-make-fulldeps/extern-flag-disambiguates/d.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg(before)] extern crate a;
extern crate b;
extern crate c;
#[cfg(after)] extern crate a;

fn t(a: &'static usize) -> usize { a as *const _ as usize }

fn main() {
    assert_eq!(t(a::token()), t(b::a_token()));
    assert!(t(a::token()) != t(c::a_token()));
}


