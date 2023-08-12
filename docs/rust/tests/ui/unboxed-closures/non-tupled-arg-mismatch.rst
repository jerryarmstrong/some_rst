tests/ui/unboxed-closures/non-tupled-arg-mismatch.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unboxed_closures)]

fn a<F: Fn<usize>>(f: F) {}
//~^ ERROR type parameter to bare `Fn` trait must be a tuple

fn main() {
    a(|_: usize| {});
}


