tests/ui/typeck/explain_clone_autoref.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct NotClone;

fn main() {
    clone_thing(&NotClone);
}

fn clone_thing(nc: &NotClone) -> NotClone {
    //~^ NOTE expected `NotClone` because of return type
    nc.clone()
    //~^ ERROR mismatched type
    //~| NOTE `NotClone` does not implement `Clone`, so `&NotClone` was cloned instead
    //~| NOTE expected struct `NotClone`, found `&NotClone`
}


