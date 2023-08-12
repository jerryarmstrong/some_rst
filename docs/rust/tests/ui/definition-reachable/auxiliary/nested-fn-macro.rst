tests/ui/definition-reachable/auxiliary/nested-fn-macro.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

mod n {
    pub(crate) mod p {
        pub fn f() -> i32 { 12 }
    }
}

pub macro m() {
    n::p::f()
}


