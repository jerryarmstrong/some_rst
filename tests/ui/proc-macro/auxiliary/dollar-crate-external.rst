tests/ui/proc-macro/auxiliary/dollar-crate-external.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub type S = u8;

#[macro_export]
macro_rules! external {
    () => {
        print_bang! {
            struct M($crate::S);
        }

        #[print_attr]
        struct A($crate::S);

        #[derive(Print)]
        struct D($crate::S);
    };
}

#[macro_export]
macro_rules! issue_62325 { () => {
    #[print_attr]
    struct B(identity!($crate::S));
}}


