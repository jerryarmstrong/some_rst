tests/run-make-fulldeps/mixing-deps/dylib.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "dylib"]
extern crate both;

use std::mem;

pub fn addr() -> usize { unsafe { mem::transmute(&both::foo) } }


