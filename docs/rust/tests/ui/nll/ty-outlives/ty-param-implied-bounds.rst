tests/ui/nll/ty-outlives/ty-param-implied-bounds.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Zverbose
// check-pass

// Test that we assume that universal types like `T` outlive the
// function body.

use std::cell::Cell;

fn twice<F, T>(value: T, mut f: F)
where
    F: FnMut(Cell<&T>),
{
    f(Cell::new(&value));
    f(Cell::new(&value));
}

fn generic<T>(value: T) {
    // No error here:
    twice(value, |r| invoke(r));
}

fn invoke<'a, T>(x: Cell<&'a T>)
where
    T: 'a,
{
}

fn main() {}


