tests/ui/issues/issue-6344-match.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_shorthand_field_patterns)]

struct A { x: usize }

impl Drop for A {
    fn drop(&mut self) {}
}

pub fn main() {
    let a = A { x: 0 };

    match a {
        A { x : ref x } => {
            println!("{}", x)
        }
    }
}


