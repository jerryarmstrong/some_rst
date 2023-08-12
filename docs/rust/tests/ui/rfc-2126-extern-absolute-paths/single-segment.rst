tests/ui/rfc-2126-extern-absolute-paths/single-segment.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:xcrate.rs
// compile-flags:--extern xcrate
// edition:2018

use crate; //~ ERROR crate root imports need to be explicitly named: `use crate as name;`
use *; //~ ERROR cannot glob-import all possible crates

fn main() {
    let s = ::xcrate; //~ ERROR expected value, found crate `xcrate`
                      //~^ NOTE not a value
}


