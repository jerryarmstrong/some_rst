tests/ui/mir/issue-83499-input-output-iteration-ice.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that when in MIR the amount of local_decls and amount of normalized_input_tys don't match
// that an out-of-bounds access does not occur.
#![feature(c_variadic)]

fn main() {}

fn foo(_: Bar, ...) -> impl {}
//~^ ERROR only foreign or `unsafe extern "C"` functions may be C-variadic
//~| ERROR cannot find type `Bar` in this scope
//~| ERROR at least one trait must be specified


