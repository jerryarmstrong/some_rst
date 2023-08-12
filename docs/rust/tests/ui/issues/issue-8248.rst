tests/ui/issues/issue-8248.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

trait A {
    fn dummy(&self) { }
}
struct B;
impl A for B {}

fn foo(_: &mut dyn A) {}

pub fn main() {
    let mut b = B;
    foo(&mut b as &mut dyn A);
}


