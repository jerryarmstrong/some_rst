tests/ui/proc-macro/lints_in_proc_macros.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // aux-build:bang_proc_macro2.rs

extern crate bang_proc_macro2;

use bang_proc_macro2::bang_proc_macro2;

fn main() {
    let foobar = 42;
    bang_proc_macro2!();
    //~^ ERROR cannot find value `foobar2` in this scope
    //~| HELP a local variable with a similar name exists
    //~| SUGGESTION foobar
    println!("{}", x);
}


