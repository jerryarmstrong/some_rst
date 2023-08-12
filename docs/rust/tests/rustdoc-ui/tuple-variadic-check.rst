tests/rustdoc-ui/tuple-variadic-check.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustdoc_internals)]

trait Mine {}

// This one is fine
#[doc(fake_variadic)]
impl<T> Mine for (T,) {}

trait Mine2 {}

// This one is not
#[doc(fake_variadic)] //~ ERROR
impl<T, U> Mine for (T,U) {}

fn main() {}


