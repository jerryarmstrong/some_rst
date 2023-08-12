tests/ui/generator/metadata-sufficient-for-layout.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that the layout of a generator is available when auxiliary crate
// is compiled with --emit metadata.
//
// Regression test for #80998.
//
// aux-build:metadata-sufficient-for-layout.rs

#![feature(type_alias_impl_trait, rustc_attrs)]
#![feature(generator_trait)]

extern crate metadata_sufficient_for_layout;

use std::ops::Generator;

type F = impl Generator<(), Yield = (), Return = ()>;

// Static queries the layout of the generator.
static A: Option<F> = None;

fn f() -> F {
    metadata_sufficient_for_layout::g()
}

#[rustc_error]
fn main() {} //~ ERROR


