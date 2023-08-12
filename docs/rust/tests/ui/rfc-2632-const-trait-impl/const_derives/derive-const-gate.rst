tests/ui/rfc-2632-const-trait-impl/const_derives/derive-const-gate.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive_const(Default)] //~ ERROR use of unstable library feature
pub struct S;

fn main() {}


