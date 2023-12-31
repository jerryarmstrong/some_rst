tests/ui/generator/panic-drops-resume.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //! Tests that panics inside a generator will correctly drop the initial resume argument.

// run-pass
// needs-unwind

#![feature(generators, generator_trait)]

use std::ops::Generator;
use std::panic::{catch_unwind, AssertUnwindSafe};
use std::pin::Pin;
use std::sync::atomic::{AtomicUsize, Ordering};

static DROP: AtomicUsize = AtomicUsize::new(0);

struct Dropper {}

impl Drop for Dropper {
    fn drop(&mut self) {
        DROP.fetch_add(1, Ordering::SeqCst);
    }
}

fn main() {
    let mut gen = |_arg| {
        if true {
            panic!();
        }
        yield ();
    };
    let mut gen = Pin::new(&mut gen);

    assert_eq!(DROP.load(Ordering::Acquire), 0);
    let res = catch_unwind(AssertUnwindSafe(|| gen.as_mut().resume(Dropper {})));
    assert!(res.is_err());
    assert_eq!(DROP.load(Ordering::Acquire), 1);
}


