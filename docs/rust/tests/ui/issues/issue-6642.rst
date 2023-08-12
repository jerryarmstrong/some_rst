tests/ui/issues/issue-6642.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A;
impl A {
    fn m(&self) {
        fn x() {
            self.m() //~ ERROR can't capture dynamic environment in a fn item
        }
    }
}
fn main() {}


