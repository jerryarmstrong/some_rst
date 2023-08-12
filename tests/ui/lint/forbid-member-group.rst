tests/ui/lint/forbid-member-group.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check what happens when we forbid a member of
// a group but then allow the group.

#![forbid(unused_variables)]

#[allow(unused)]
//~^ ERROR incompatible with previous forbid
//~| ERROR incompatible with previous forbid
fn main() {
    let a: ();
}


