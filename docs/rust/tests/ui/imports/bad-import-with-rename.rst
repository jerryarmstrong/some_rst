tests/ui/imports/bad-import-with-rename.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod A {
    pub type B = ();
    pub type B2 = ();
}

mod C {
    use crate::D::B as _;
    //~^ ERROR unresolved import `crate::D::B`

    use crate::D::B2;
    //~^ ERROR unresolved import `crate::D::B2`
}

mod D {}

fn main() {}


