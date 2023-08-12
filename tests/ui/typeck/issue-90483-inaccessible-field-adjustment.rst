tests/ui/typeck/issue-90483-inaccessible-field-adjustment.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

mod m {
  pub struct S { foo: i32 }
  impl S {
    pub fn foo(&self) -> i32 { 42 }
  }
}

fn bar(s: &m::S) {
  || s.foo() + s.foo; //~ ERROR E0616
}

fn main() {}


