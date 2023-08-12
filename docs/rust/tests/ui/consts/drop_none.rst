tests/ui/consts/drop_none.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
#![allow(dead_code)]
struct A;
impl Drop for A {
    fn drop(&mut self) {}
}

const FOO: Option<A> = None;

const BAR: () = (FOO, ()).1;


fn main() {}


