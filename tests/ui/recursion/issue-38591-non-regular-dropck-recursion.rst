tests/ui/recursion/issue-38591-non-regular-dropck-recursion.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // `S` is infinitely recursing so it's not possible to generate a finite
// drop impl (ignoring polymorphization).
//
// Dropck should therefore detect that this is the case and eagerly error.

struct S<T> {
    t: T,
    s: Box<S<fn(u: T)>>,
}

fn f(x: S<u32>) {} //~ ERROR overflow while adding drop-check rules for S<u32>

fn main() {
    // Force instantiation.
    f as fn(_);
}


