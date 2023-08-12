tests/ui/proc-macro/lifetimes.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:lifetimes.rs

extern crate lifetimes;

use lifetimes::*;

type A = single_quote_alone!(); //~ ERROR expected type, found `'`

fn main() {}


