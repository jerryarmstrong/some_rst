tests/incremental/remapped_paths_cc/auxiliary/extern_crate.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //[rpass1] compile-flags: -g
//[rpass2] compile-flags: -g
//[rpass3] compile-flags: -g --remap-path-prefix={{src-base}}=/the/src

#![feature(rustc_attrs)]
#![crate_type="rlib"]

#[inline(always)]
pub fn inline_fn() {
    println!("test");
}


