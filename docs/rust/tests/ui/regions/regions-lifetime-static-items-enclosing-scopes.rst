tests/ui/regions/regions-lifetime-static-items-enclosing-scopes.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// This test verifies that temporary lifetime is correctly computed
// for static objects in enclosing scopes.


use std::cmp::PartialEq;

fn f<T:PartialEq+std::fmt::Debug>(o: &mut Option<T>) {
    assert_eq!(*o, None);
}

pub fn main() {
    mod t {
        enum E {V=1, A=0}
        static C: E = E::V;
    }

    f::<isize>(&mut None);
}


