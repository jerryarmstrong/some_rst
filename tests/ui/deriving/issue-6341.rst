tests/ui/deriving/issue-6341.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// pretty-expanded FIXME #23616

#[derive(PartialEq)]
struct A { x: usize }

impl Drop for A {
    fn drop(&mut self) {}
}

pub fn main() {}


