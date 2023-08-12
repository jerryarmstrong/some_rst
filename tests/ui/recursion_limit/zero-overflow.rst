tests/ui/recursion_limit/zero-overflow.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //~ ERROR overflow evaluating the requirement `&mut Self: DispatchFromDyn<&mut RustaceansAreAwesome>
//~| HELP consider increasing the recursion limit
// build-fail

#![recursion_limit = "0"]

fn main() {}


