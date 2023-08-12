tests/ui/coherence/re-rebalance-coherence.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:re_rebalance_coherence_lib.rs

extern crate re_rebalance_coherence_lib as lib;
use lib::*;

struct Oracle;
impl Backend for Oracle {}
impl<'a, T:'a, Tab> QueryFragment<Oracle> for BatchInsert<'a, T, Tab> {}

fn main() {}


