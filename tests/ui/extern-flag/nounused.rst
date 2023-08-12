tests/ui/extern-flag/nounused.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-crate:nounused:somedep=somedep.rs
// compile-flags: -Zunstable-options -Dunused-crate-dependencies
// edition:2018

fn main() {
}


