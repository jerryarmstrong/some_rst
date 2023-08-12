tests/ui/consts/issue-67696-const-prop-ice.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: --emit=mir,link
// Checks that we don't ICE due to attempting to run const prop
// on a function with unsatisifable 'where' clauses

#![allow(unused)]

trait A {
    fn foo(&self) -> Self where Self: Copy;
}

impl A for [fn(&())] {
    fn foo(&self) -> Self where Self: Copy { *(&[] as &[_]) }
}

impl A for i32 {
    fn foo(&self) -> Self { 3 }
}

fn main() {}


