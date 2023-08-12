tests/ui/privacy/pub_use_mods_xcrate_exe.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:pub_use_mods_xcrate.rs

// pretty-expanded FIXME #23616

#![allow(unused_imports)]

extern crate pub_use_mods_xcrate;
use pub_use_mods_xcrate::a::c;

pub fn main(){}


