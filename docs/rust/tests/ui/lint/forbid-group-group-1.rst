tests/ui/lint/forbid-group-group-1.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check what happens when we forbid a smaller group but
// then allow a superset of that group.

#![forbid(nonstandard_style)]

// FIXME: Arguably this should be an error, but the WARNINGS group is
// treated in a very special (and rather ad-hoc) way and
// it fails to trigger.
#[allow(warnings)]
fn main() {
    let A: ();
    //~^ ERROR should have a snake case name
}


