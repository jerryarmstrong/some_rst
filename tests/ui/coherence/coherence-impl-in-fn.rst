tests/ui/coherence/coherence-impl-in-fn.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

pub fn main() {
    #[derive(Copy, Clone)]
    enum x { foo }
    impl ::std::cmp::PartialEq for x {
        fn eq(&self, other: &x) -> bool {
            (*self) as isize == (*other) as isize
        }
        fn ne(&self, other: &x) -> bool { !(*self).eq(other) }
    }
}


