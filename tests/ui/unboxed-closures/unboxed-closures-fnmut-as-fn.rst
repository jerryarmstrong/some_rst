tests/ui/unboxed-closures/unboxed-closures-fnmut-as-fn.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that the Fn trait hierarchy rules do not permit
// Fn to be used where FnMut is implemented.

#![feature(fn_traits, unboxed_closures)]

use std::ops::{Fn,FnMut,FnOnce};

struct S;

impl FnMut<(isize,)> for S {
    extern "rust-call" fn call_mut(&mut self, (x,): (isize,)) -> isize {
        x * x
    }
}

impl FnOnce<(isize,)> for S {
    type Output = isize;

    extern "rust-call" fn call_once(mut self, args: (isize,)) -> isize { self.call_mut(args) }
}

fn call_it<F:Fn(isize)->isize>(f: &F, x: isize) -> isize {
    f.call((x,))
}

fn main() {
    let x = call_it(&S, 22);
    //~^ ERROR E0277
}


