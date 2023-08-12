src/tools/clippy/tests/ui/err_expect.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused)]

struct MyTypeNonDebug;

#[derive(Debug)]
struct MyTypeDebug;

fn main() {
    let test_debug: Result<MyTypeDebug, u32> = Ok(MyTypeDebug);
    test_debug.err().expect("Testing debug type");

    let test_non_debug: Result<MyTypeNonDebug, u32> = Ok(MyTypeNonDebug);
    test_non_debug.err().expect("Testing non debug type");
}

#[clippy::msrv = "1.16"]
fn msrv_1_16() {
    let x: Result<u32, &str> = Ok(16);
    x.err().expect("16");
}

#[clippy::msrv = "1.17"]
fn msrv_1_17() {
    let x: Result<u32, &str> = Ok(17);
    x.err().expect("17");
}


