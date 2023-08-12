tests/ui/underscore-lifetime/dyn-trait-underscore-in-struct.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that the `'_` in `dyn Trait + '_` acts like ordinary elision,
// and not like an object lifetime default.
//
// cc #48468

use std::fmt::Debug;

struct Foo {
    x: Box<dyn Debug + '_>, //~ ERROR missing lifetime specifier
}

fn main() {}


