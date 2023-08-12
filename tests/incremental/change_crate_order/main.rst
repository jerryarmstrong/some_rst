tests/incremental/change_crate_order/main.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:a.rs
// aux-build:b.rs
// revisions:rpass1 rpass2

#![feature(rustc_attrs)]


#[cfg(rpass1)]
extern crate a;
#[cfg(rpass1)]
extern crate b;

#[cfg(rpass2)]
extern crate b;
#[cfg(rpass2)]
extern crate a;

use a::A;
use b::B;

//? #[rustc_clean(label="typeck", cfg="rpass2")]
pub fn main() {
    A + B;
}


