src/tools/miri/tests/pass/issues/issue-miri-1925.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //@compile-flags: -Zmiri-symbolic-alignment-check

use std::mem::size_of;

fn main() {
    let mut a = Params::new();
    a.key_block = [0; BLOCKBYTES];
}

#[repr(C)]
#[derive(Clone)]
#[allow(unused)]
pub struct Params {
    hash_length: u8,
    key_length: u8,
    key_block: [u8; BLOCKBYTES],
    max_leaf_length: u32,
}

pub const OUTBYTES: usize = 8 * size_of::<u64>();
pub const KEYBYTES: usize = 8 * size_of::<u64>();
pub const BLOCKBYTES: usize = 16 * size_of::<u64>();

impl Params {
    pub fn new() -> Self {
        Self {
            hash_length: OUTBYTES as u8,
            key_length: 0,
            key_block: [0; BLOCKBYTES],
            max_leaf_length: 0,
        }
    }
}


