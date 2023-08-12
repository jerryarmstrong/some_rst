tests/run-make-fulldeps/metadata-flag-frobs-symbols/foo.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "foo"]
#![crate_type = "rlib"]

static FOO: usize = 3;

pub fn foo() -> &'static usize { &FOO }


