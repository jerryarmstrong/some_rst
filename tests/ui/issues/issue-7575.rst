tests/ui/issues/issue-7575.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo {
    fn new() -> bool { false }
    fn dummy(&self) { }
}

trait Bar {
    fn new(&self) -> bool { true }
}

impl Bar for isize {}
impl Foo for isize {}

fn main() {
    assert!(1.new());
}


