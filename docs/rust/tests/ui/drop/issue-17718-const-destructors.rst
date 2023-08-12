tests/ui/drop/issue-17718-const-destructors.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
struct A;
impl Drop for A {
    fn drop(&mut self) {}
}

const FOO: A = A;

fn main() {}


