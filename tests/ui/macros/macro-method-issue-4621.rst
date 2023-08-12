tests/ui/macros/macro-method-issue-4621.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct A;

macro_rules! make_thirteen_method {() => (fn thirteen(&self)->isize {13})}
impl A { make_thirteen_method!(); }

fn main() {
    assert_eq!(A.thirteen(),13);
}


