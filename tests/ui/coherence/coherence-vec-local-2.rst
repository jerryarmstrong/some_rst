tests/ui/coherence/coherence-vec-local-2.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a local, generic type appearing within a
// *non-fundamental* remote type like `Vec` is not considered local.

// aux-build:coherence_lib.rs

extern crate coherence_lib as lib;
use lib::Remote;

struct Local<T>(T);

impl<T> Remote for Vec<Local<T>> { }
//~^ ERROR E0117

fn main() { }


