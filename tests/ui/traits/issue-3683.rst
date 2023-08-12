tests/ui/traits/issue-3683.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo {
    fn a(&self) -> isize;
    fn b(&self) -> isize {
        self.a() + 2
    }
}

impl Foo for isize {
    fn a(&self) -> isize {
        3
    }
}

pub fn main() {
    assert_eq!(3.b(), 5);
}


