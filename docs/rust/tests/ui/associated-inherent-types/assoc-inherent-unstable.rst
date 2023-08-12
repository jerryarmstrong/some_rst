tests/ui/associated-inherent-types/assoc-inherent-unstable.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-crate:aux=assoc-inherent-unstable.rs
// edition: 2021

type Data = aux::Owner::Data; //~ ERROR use of unstable library feature 'data'

fn main() {}


