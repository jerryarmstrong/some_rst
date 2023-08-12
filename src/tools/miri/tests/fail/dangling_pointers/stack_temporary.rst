src/tools/miri/tests/fail/dangling_pointers/stack_temporary.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This should fail even without validation, but some MIR opts mask the error
//@compile-flags: -Zmiri-disable-validation -Zmir-opt-level=0

unsafe fn make_ref<'a>(x: *mut i32) -> &'a mut i32 {
    &mut *x
}

fn main() {
    unsafe {
        let x = make_ref(&mut 0); // The temporary storing "0" is deallocated at the ";"!
        let val = *x; //~ ERROR: dereferenced after this allocation got freed
        println!("{}", val);
    }
}


