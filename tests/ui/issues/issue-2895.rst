tests/ui/issues/issue-2895.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]

use std::mem;

struct Cat {
    x: isize
}

struct Kitty {
    x: isize,
}

impl Drop for Kitty {
    fn drop(&mut self) {}
}

#[cfg(target_pointer_width = "64")]
pub fn main() {
    assert_eq!(mem::size_of::<Cat>(), 8 as usize);
    assert_eq!(mem::size_of::<Kitty>(), 8 as usize);
}

#[cfg(target_pointer_width = "32")]
pub fn main() {
    assert_eq!(mem::size_of::<Cat>(), 4 as usize);
    assert_eq!(mem::size_of::<Kitty>(), 4 as usize);
}


