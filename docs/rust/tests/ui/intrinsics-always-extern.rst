tests/ui/intrinsics-always-extern.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(intrinsics)]

trait Foo {
    extern "rust-intrinsic" fn foo(&self); //~ ERROR intrinsic must
}

impl Foo for () {
    extern "rust-intrinsic" fn foo(&self) { //~ ERROR intrinsic must
    }
}

extern "rust-intrinsic" fn hello() {//~ ERROR intrinsic must
}

fn main() {
}


