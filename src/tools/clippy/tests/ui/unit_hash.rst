src/tools/clippy/tests/ui/unit_hash.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::unit_hash)]
#![allow(clippy::let_unit_value)]

use std::collections::hash_map::DefaultHasher;
use std::hash::Hash;

enum Foo {
    Empty,
    WithValue(u8),
}

fn do_nothing() {}

fn main() {
    let mut state = DefaultHasher::new();
    let my_enum = Foo::Empty;

    match my_enum {
        Foo::Empty => ().hash(&mut state),
        Foo::WithValue(x) => x.hash(&mut state),
    }

    let res = ();
    res.hash(&mut state);

    #[allow(clippy::unit_arg)]
    do_nothing().hash(&mut state);
}


