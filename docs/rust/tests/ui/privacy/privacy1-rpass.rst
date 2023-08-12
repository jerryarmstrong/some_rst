tests/ui/privacy/privacy1-rpass.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616

pub mod test2 {
    // This used to generate an ICE (make sure that default functions are
    // parented to their trait to find the first private thing as the trait).

    struct B;
    trait A { fn foo(&self) {} }
    impl A for B {}

    mod tests {
        use super::A;
        fn foo() {
            let a = super::B;
            a.foo();
        }
    }
}


pub fn main() {}


