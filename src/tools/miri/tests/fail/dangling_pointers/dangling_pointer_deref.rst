src/tools/miri/tests/fail/dangling_pointers/dangling_pointer_deref.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Make sure we find these even with many checks disabled.
//@compile-flags: -Zmiri-disable-alignment-check -Zmiri-disable-stacked-borrows -Zmiri-disable-validation

fn main() {
    let p = {
        let b = Box::new(42);
        &*b as *const i32
    };
    let x = unsafe { *p }; //~ ERROR: dereferenced after this allocation got freed
    panic!("this should never print: {}", x);
}


