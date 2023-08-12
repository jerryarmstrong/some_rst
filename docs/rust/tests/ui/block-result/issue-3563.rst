tests/ui/block-result/issue-3563.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait A {
    fn a(&self) {
        || self.b()
        //~^ ERROR no method named `b` found
    }
}
fn main() {}


