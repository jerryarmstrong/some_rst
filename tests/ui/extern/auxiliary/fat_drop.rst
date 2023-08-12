tests/ui/extern/auxiliary/fat_drop.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub static mut DROPPED: bool = false;

pub struct S {
    _unsized: [u8]
}

impl Drop for S {
    fn drop(&mut self) {
        unsafe {
            DROPPED = true;
        }
    }
}


