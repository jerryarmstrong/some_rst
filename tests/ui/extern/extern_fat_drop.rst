tests/ui/extern/extern_fat_drop.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:fat_drop.rs

extern crate fat_drop;

fn main() {
    unsafe {
        let data: &mut [u8] = &mut [0];
        let s: &mut fat_drop::S = std::mem::transmute::<&mut [u8], _>(data);
        std::ptr::drop_in_place(s);
        assert!(fat_drop::DROPPED);
    }
}


