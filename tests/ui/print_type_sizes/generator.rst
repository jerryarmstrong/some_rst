tests/ui/print_type_sizes/generator.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z print-type-sizes --crate-type=lib
// build-pass
// ignore-pass

#![feature(generators, generator_trait)]

use std::ops::Generator;

fn generator<const C: usize>(array: [u8; C]) -> impl Generator<Yield = (), Return = ()> {
    move |()| {
        yield ();
        let _ = array;
    }
}

pub fn foo() {
    let _ = generator([0; 8192]);
}


