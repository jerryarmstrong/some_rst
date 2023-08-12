tests/ui/consts/promoted-const-drop.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]
#![feature(const_mut_refs)]

struct A();

impl const Drop for A {
    fn drop(&mut self) {}
}

const C: A = A();

fn main() {
    let _: &'static A = &A(); //~ ERROR temporary value dropped while borrowed
    let _: &'static [A] = &[C]; //~ ERROR temporary value dropped while borrowed
}


