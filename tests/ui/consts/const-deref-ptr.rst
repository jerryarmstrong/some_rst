tests/ui/consts/const-deref-ptr.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that you can't dereference invalid raw pointers in constants.

fn main() {
    static C: u64 = unsafe {*(0xdeadbeef as *const u64)};
    //~^ ERROR could not evaluate static initializer
    println!("{}", C);
}


