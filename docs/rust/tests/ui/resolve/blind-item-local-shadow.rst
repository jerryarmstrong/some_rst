tests/ui/resolve/blind-item-local-shadow.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
#![allow(unused_imports)]
mod bar {
    pub fn foo() -> bool { true }
}

fn main() {
    let foo = || false;
    use bar::foo;
    assert_eq!(foo(), false);
}


