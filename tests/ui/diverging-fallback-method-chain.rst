tests/ui/diverging-fallback-method-chain.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(unused_imports)]
// Test a regression found when building compiler. The `produce()`
// error type `T` winds up getting unified with result of `x.parse()`;
// the type of the closure given to `unwrap_or_else` needs to be
// inferred to `usize`.

use std::num::ParseIntError;

fn produce<T>() -> Result<&'static str, T> {
    Ok("22")
}

fn main() {
    let x: usize = produce()
        .and_then(|x| x.parse())
        .unwrap_or_else(|_| panic!());
    println!("{}", x);
}


