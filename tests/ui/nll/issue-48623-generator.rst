tests/ui/nll/issue-48623-generator.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(path_statements)]
#![allow(dead_code)]

#![feature(generators, generator_trait)]

struct WithDrop;

impl Drop for WithDrop {
    fn drop(&mut self) {}
}

fn reborrow_from_generator(r: &mut ()) {
    let d = WithDrop;
    move || { d; yield; &mut *r }; //~ WARN unused generator that must be used
}

fn main() {}


