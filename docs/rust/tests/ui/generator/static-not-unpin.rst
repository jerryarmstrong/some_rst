tests/ui/generator/static-not-unpin.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generators)]

// normalize-stderr-test "std::pin::Unpin" -> "std::marker::Unpin"

use std::marker::Unpin;

fn assert_unpin<T: Unpin>(_: T) {
}

fn main() {
    let mut generator = static || {
        yield;
    };
    assert_unpin(generator); //~ ERROR E0277
}


