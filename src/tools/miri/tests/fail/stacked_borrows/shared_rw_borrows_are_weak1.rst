src/tools/miri/tests/fail/stacked_borrows/shared_rw_borrows_are_weak1.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // We want to test that granting a SharedReadWrite will be added
// *below* an already granted Unique -- so writing to
// the SharedReadWrite will invalidate the Unique.

use std::cell::Cell;
use std::mem;

fn main() {
    unsafe {
        let x = &mut Cell::new(0);
        let y: &mut Cell<i32> = mem::transmute(&mut *x); // launder lifetime
        let shr_rw = &*x; // thanks to interior mutability this will be a SharedReadWrite
        shr_rw.set(1);
        y.get_mut(); //~ ERROR: /retag .* tag does not exist in the borrow stack/
    }
}


