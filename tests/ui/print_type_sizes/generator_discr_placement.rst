tests/ui/print_type_sizes/generator_discr_placement.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z print-type-sizes --crate-type lib
// build-pass
// ignore-pass

// Tests a generator that has its discriminant as the *final* field.

// Avoid emitting panic handlers, like the rest of these tests...
#![feature(generators)]

pub fn foo() {
    let a = || {
        {
            let w: i32 = 4;
            yield;
            drop(w);
        }
        {
            let z: i32 = 7;
            yield;
            drop(z);
        }
    };
}


