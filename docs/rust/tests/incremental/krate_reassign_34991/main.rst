tests/incremental/krate_reassign_34991/main.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:a.rs
// revisions:rpass1 rpass2

#![feature(rustc_attrs)]

#[cfg(rpass1)]
extern crate a;

#[cfg(rpass1)]
pub fn use_X() -> u32 {
    let x: a::X = 22;
    x as u32
}

#[cfg(rpass2)]
pub fn use_X() -> u32 {
    22
}

pub fn main() { }


