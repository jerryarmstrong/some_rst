tests/mir-opt/building/receiver_ptr_mutability.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // EMIT_MIR receiver_ptr_mutability.main.built.after.mir

#![feature(arbitrary_self_types)]

struct Test {}

impl Test {
    fn x(self: *const Self) {
        println!("x called");
    }
}

fn main() {
    let ptr: *mut Test = std::ptr::null_mut();
    ptr.x();

    // Test autoderefs
    let ptr_ref: &&&&*mut Test = &&&&ptr;
    ptr_ref.x();
}


