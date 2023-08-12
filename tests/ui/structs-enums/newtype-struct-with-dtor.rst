tests/ui/structs-enums/newtype-struct-with-dtor.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_unsafe)]
#![allow(unused_variables)]
// pretty-expanded FIXME #23616

pub struct Fd(u32);

fn foo(a: u32) {}

impl Drop for Fd {
    fn drop(&mut self) {
        unsafe {
            let Fd(s) = *self;
            foo(s);
        }
    }
}

pub fn main() {
}


