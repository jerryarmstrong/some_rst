tests/ui/derives/derive-deadlock.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std as derive;

#[derive(Default)] //~ ERROR cannot determine resolution for the attribute macro `derive`
struct S;

fn main() {}


