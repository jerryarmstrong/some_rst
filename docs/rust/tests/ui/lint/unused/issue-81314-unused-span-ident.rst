tests/ui/lint/unused/issue-81314-unused-span-ident.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
// Regression test for #81314: Unused variable lint should
// span only the identifier and not the rest of the pattern

#![deny(unused)]

fn main() {
    let [rest @ ..] = [1, 2, 3]; //~ ERROR unused variable
}

pub fn foo([rest @ ..]: &[i32]) { //~ ERROR unused variable
}


