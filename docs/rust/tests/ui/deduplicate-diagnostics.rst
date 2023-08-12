tests/ui/deduplicate-diagnostics.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: duplicate deduplicate
//[deduplicate] compile-flags: -Z deduplicate-diagnostics=yes

#[derive(Unresolved)] //~ ERROR cannot find derive macro `Unresolved` in this scope
                      //[duplicate]~| ERROR cannot find derive macro `Unresolved` in this scope
struct S;

#[deny("literal")] //~ ERROR malformed lint attribute input
                   //[duplicate]~| ERROR malformed lint attribute input
fn main() {}


