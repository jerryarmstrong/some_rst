tests/ui/did_you_mean/issue-93210-ignore-doc-hidden.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Default)]
pub struct A {
    #[doc(hidden)]
    pub hello: i32,
    pub bye: i32,
}

#[derive(Default)]
pub struct B {
    pub hello: i32,
    pub bye: i32,
}

fn main() {
    A::default().hey;
    //~^ ERROR no field `hey` on type `A`
    //~| NOTE unknown field
    //~| NOTE available fields are: `bye`

    B::default().hey;
    //~^ ERROR no field `hey` on type `B`
    //~| NOTE unknown field
    //~| NOTE available fields are: `hello`, `bye`
}


