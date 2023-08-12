tests/ui/lint/lint-impl-fn.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(while_true)]
#![allow(dead_code)]

struct A(isize);

impl A {
    fn foo(&self) { while true {} }

    #[deny(while_true)]
    fn bar(&self) { while true {} } //~ ERROR: infinite loops
}

#[deny(while_true)]
mod foo {
    struct B(isize);

    impl B {
        fn foo(&self) { while true {} } //~ ERROR: infinite loops

        #[allow(while_true)]
        fn bar(&self) { while true {} }
    }
}

#[deny(while_true)]
fn main() {
    while true {} //~ ERROR: infinite loops
}

#[deny(while_true)]
fn bar() {
    while cfg!(unix) {} // no error
}


