src/tools/miri/tests/fail/dangling_pointers/dangling_pointer_addr_of.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we find these even with many checks disabled.
//@compile-flags: -Zmiri-disable-alignment-check -Zmiri-disable-stacked-borrows -Zmiri-disable-validation
use std::ptr;

fn main() {
    let p = {
        let b = Box::new(42);
        &*b as *const i32
    };
    let x = unsafe { ptr::addr_of!(*p) }; //~ ERROR: dereferenced after this allocation got freed
    panic!("this should never print: {:?}", x);
}


