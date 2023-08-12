tests/ui/error-codes/e0119/complex-impl.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:complex_impl_support.rs

extern crate complex_impl_support;

use complex_impl_support::{External, M};

struct Q;

impl<R> External for (Q, R) {} //~ ERROR only traits defined

fn main() {}


