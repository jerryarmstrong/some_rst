tests/ui/traits/negative-impls/negated-auto-traits-rpass.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
#![feature(negative_impls)]

use std::marker::Send;

pub struct WaitToken;
impl !Send for WaitToken {}

pub struct Test<T>(#[allow(unused_tuple_struct_fields)] T);
unsafe impl<T: 'static> Send for Test<T> {}

pub fn spawn<F>(_: F) -> () where F: FnOnce(), F: Send + 'static {}

fn main() {
    let wt = Test(WaitToken);
    spawn(move || {
        let x = wt;
        println!("Hello, World!");
    });
}


