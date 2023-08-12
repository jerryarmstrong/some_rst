tests/ui/extern-flag/no-nounused.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-crate:somedep=somedep.rs
// compile-flags: -Zunstable-options -Dunused-crate-dependencies
// edition:2018

fn main() { //~ ERROR external crate `somedep` unused in `no_nounused`
}


