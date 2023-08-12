tests/ui/async-await/issue-74497-lifetime-in-opaque.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

// test that names give to anonymous lifetimes in opaque types like `impl Future` are correctly
// introduced in error messages

use std::future::Future;

pub async fn foo<F, T>(_: F)
where
    F: Fn(&u8) -> T,
    T: Future<Output = ()>,
{
}

pub async fn bar(_: &u8) {}

fn main() {
    let _ = foo(|x| bar(x)); //~ ERROR lifetime may not live long enough
}


