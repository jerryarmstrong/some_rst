tests/ui/lint/forbid-group-member.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check what happens when we forbid a group but
// then allow a member of that group.
//
// check-pass

#![forbid(unused)]

#[allow(unused_variables)]
//~^ WARNING incompatible with previous forbid
//~| WARNING previously accepted
//~| WARNING incompatible with previous forbid
//~| WARNING previously accepted
//~| WARNING incompatible with previous forbid
//~| WARNING previously accepted
fn main() {
    let a: ();
}


