tests/ui/unresolved/unresolved-extern-mod-suggestion.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate core;
use core;
//~^ ERROR the name `core` is defined multiple times

fn main() {}


