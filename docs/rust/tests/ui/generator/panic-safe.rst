tests/ui/generator/panic-safe.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// needs-unwind


#![feature(generators, generator_trait)]

use std::ops::Generator;
use std::pin::Pin;
use std::panic;

fn main() {
    let mut foo = || {
        if true {
            panic!();
        }
        yield;
    };

    let res = panic::catch_unwind(panic::AssertUnwindSafe(|| {
        Pin::new(&mut foo).resume(())
    }));
    assert!(res.is_err());

    for _ in 0..10 {
        let res = panic::catch_unwind(panic::AssertUnwindSafe(|| {
            Pin::new(&mut foo).resume(())
        }));
        assert!(res.is_err());
    }
}


