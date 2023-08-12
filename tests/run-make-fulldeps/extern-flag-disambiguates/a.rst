tests/run-make-fulldeps/extern-flag-disambiguates/a.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "a"]
#![crate_type = "rlib"]

static FOO: usize = 3;

pub fn token() -> &'static usize { &FOO }


