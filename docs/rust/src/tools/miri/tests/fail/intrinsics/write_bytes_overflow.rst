src/tools/miri/tests/fail/intrinsics/write_bytes_overflow.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

fn main() {
    let mut y = 0;
    unsafe {
        (&mut y as *mut i32).write_bytes(0u8, 1usize << (mem::size_of::<usize>() * 8 - 1));
        //~^ ERROR: overflow computing total size of `write_bytes`
    }
}


