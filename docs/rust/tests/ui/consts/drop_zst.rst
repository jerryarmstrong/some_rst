tests/ui/consts/drop_zst.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-fail

#![feature(const_precise_live_drops)]

struct S;

impl Drop for S {
    fn drop(&mut self) {
        println!("Hello!");
    }
}

const fn foo() {
    let s = S; //~ destructor
}

fn main() {}


