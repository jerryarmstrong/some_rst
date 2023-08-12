tests/ui/lifetimes/issue-76168-hr-outlives.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// check-pass

#![feature(unboxed_closures)]
use std::future::Future;

async fn wrapper<F>(f: F)
where for<'a> F: FnOnce<(&'a mut i32,)>,
    for<'a> <F as FnOnce<(&'a mut i32,)>>::Output: Future<Output=()> + 'a
{
    let mut i = 41;
    f(&mut i).await;
}

async fn add_one(i: &mut i32) {
    *i = *i + 1;
}

fn main() {}


