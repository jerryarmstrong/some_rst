tests/ui/async-await/bound-normalization.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// edition:2018

// See issue 60414

trait Trait {
    type Assoc;
}

async fn foo<T: Trait<Assoc=()>>() -> T::Assoc {
    ()
}

fn main() {}


