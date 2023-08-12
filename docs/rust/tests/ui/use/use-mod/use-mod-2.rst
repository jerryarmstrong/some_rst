tests/ui/use/use-mod/use-mod-2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    use self::{self};
    //~^ ERROR unresolved import `self` [E0432]
    //~| no `self` in the root

    use super::{self};
    //~^ ERROR unresolved import `super` [E0432]
    //~| no `super` in the root
}

fn main() {}


