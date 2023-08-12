tests/ui/packed/packed-with-inference-vars-issue-61402.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// If a struct is packed and its last field has drop glue, then that
// field needs to be Sized (to allow it to be destroyed out-of-place).
//
// This is checked by the compiler during wfcheck. That check used
// to have problems with associated types in the last field - test
// that this doesn't ICE.

#![allow(unused_imports, dead_code)]

pub struct S;

pub trait Trait<R> { type Assoc; }

impl<X> Trait<X> for S { type Assoc = X; }

#[repr(C, packed)]
struct PackedAssocSized {
    pos: Box<<S as Trait<usize>>::Assoc>,
}

fn main() { println!("Hello, world!"); }


