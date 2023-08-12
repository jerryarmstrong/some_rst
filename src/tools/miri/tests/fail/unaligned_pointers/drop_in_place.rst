src/tools/miri/tests/fail/unaligned_pointers/drop_in_place.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(transparent)]
struct HasDrop(u8);

impl Drop for HasDrop {
    fn drop(&mut self) {}
}

#[repr(C, align(2))]
struct PartialDrop {
    a: HasDrop,
    b: u8,
}

//@error-pattern: /alignment 2 is required/
fn main() {
    unsafe {
        // Create an unaligned pointer
        let mut x = [0_u16; 2];
        let p = core::ptr::addr_of_mut!(x).cast::<u8>();
        let p = p.add(1);
        let p = p.cast::<PartialDrop>();

        core::ptr::drop_in_place(p);
    }
}


