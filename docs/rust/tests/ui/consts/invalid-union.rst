tests/ui/consts/invalid-union.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that constants with interior mutability inside unions are rejected
// during validation.
//
// Note that this test case relies on undefined behaviour to construct a
// constant with interior mutability that is "invisible" to the static checks.
// If for some reason this approach no longer works, it is should be fine to
// remove the test case.
//
// build-fail
// stderr-per-bitwidth
#![feature(const_mut_refs)]

use std::cell::Cell;
use std::mem::ManuallyDrop;

#[repr(C)]
struct S {
    x: u32,
    y: E,
}

#[repr(u32)]
enum E {
    A,
    B(U)
}

union U {
    cell: ManuallyDrop<Cell<u32>>,
}

const C: S = {
    let s = S { x: 0, y: E::A };
    // Go through an &u32 reference which is definitely not allowed to mutate anything.
    let p = &s.x as *const u32 as *mut u32;
    // Change enum tag to E::B.
    unsafe { *p.add(1) = 1 };
    s
};

fn main() { //~ ERROR it is undefined behavior to use this value
    // FIXME the span here is wrong, sould be pointing at the line below, not above.
    let _: &'static _ = &C;
}


