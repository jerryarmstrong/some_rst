tests/ui/definition-reachable/auxiliary/private-use-macro.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(decl_macro)]

mod n {
    pub static S: i32 = 57;
}

use n::S;

pub macro m() {
    S
}


