tests/ui/async-await/no-unsafe-async.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

struct S;

impl S {
    #[cfg(FALSE)]
    unsafe async fn g() {} //~ ERROR expected one of `extern` or `fn`, found keyword `async`
}

#[cfg(FALSE)]
unsafe async fn f() {} //~ ERROR expected one of `extern` or `fn`, found keyword `async`


