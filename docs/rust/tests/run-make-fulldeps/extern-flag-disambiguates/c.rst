tests/run-make-fulldeps/extern-flag-disambiguates/c.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "c"]
#![crate_type = "rlib"]

extern crate a;

static FOO: usize = 3;

pub fn token() -> &'static usize { &FOO }
pub fn a_token() -> &'static usize { a::token() }


