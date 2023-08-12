tests/ui/nll/issue-48623-closure.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(path_statements)]
#![allow(dead_code)]

struct WithDrop;

impl Drop for WithDrop {
    fn drop(&mut self) {}
}

fn reborrow_from_closure(r: &mut ()) -> &mut () {
    let d = WithDrop;
    (move || { d; &mut *r })()
}

fn main() {}


