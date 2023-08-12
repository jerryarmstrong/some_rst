tests/ui/never_type/never_transmute_never.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#![crate_type="lib"]

#![feature(never_type)]
#![allow(dead_code)]
#![allow(unreachable_code)]
#![allow(unused_variables)]

struct Foo;

pub fn f(x: !) -> ! {
    x
}

pub fn ub() {
    // This is completely undefined behaviour,
    // but we still want to make sure it compiles.
    let x: ! = unsafe {
        std::mem::transmute::<Foo, !>(Foo)
    };
    f(x)
}


