src/tools/clippy/tests/ui/swap_ptr_to_ref_unfixable.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::swap_ptr_to_ref)]

macro_rules! addr_of_mut_to_ref {
    ($e:expr) => {
        &mut *core::ptr::addr_of_mut!($e)
    };
}

fn main() {
    let mut x = 0u32;
    let y: *mut _ = &mut x;

    unsafe {
        core::mem::swap(addr_of_mut_to_ref!(x), &mut *y);
        core::mem::swap(&mut *y, addr_of_mut_to_ref!(x));
        core::mem::swap(addr_of_mut_to_ref!(x), addr_of_mut_to_ref!(x));
    }
}


