tests/ui/consts/static_mut_containing_mut_ref2.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: stock mut_refs

#![cfg_attr(mut_refs, feature(const_mut_refs))]

static mut STDERR_BUFFER_SPACE: u8 = 0;

pub static mut STDERR_BUFFER: () = unsafe { *(&mut STDERR_BUFFER_SPACE) = 42; };
//[mut_refs]~^ ERROR could not evaluate static initializer
//[stock]~^^ ERROR mutable references are not allowed in statics

fn main() {}


