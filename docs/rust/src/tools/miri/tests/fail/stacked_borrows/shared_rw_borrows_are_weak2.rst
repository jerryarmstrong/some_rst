src/tools/miri/tests/fail/stacked_borrows/shared_rw_borrows_are_weak2.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We want to test that granting a SharedReadWrite will be added
// *below* an already granted SharedReadWrite -- so writing to
// the SharedReadWrite will invalidate the SharedReadWrite.
//@normalize-stderr-test: "0x[0-9a-fA-F]+" -> "$$HEX"

use std::cell::RefCell;
use std::mem;

fn main() {
    unsafe {
        let x = &mut RefCell::new(0);
        let y: &i32 = mem::transmute(&*x.borrow()); // launder lifetime
        let shr_rw = &*x; // thanks to interior mutability this will be a SharedReadWrite
        shr_rw.replace(1);
        let _val = *y; //~ ERROR: /read access .* tag does not exist in the borrow stack/
    }
}


