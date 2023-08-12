tests/ui/extern/extern-prelude-no-speculative.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
// compile-flags: --extern LooksLikeExternCrate=/path/to/nowhere

mod m {
    pub struct LooksLikeExternCrate;
}

fn main() {
    // OK, speculative resolution for `unused_qualifications` doesn't try
    // to resolve this as an extern crate and load that crate
    let s = m::LooksLikeExternCrate {};
}


