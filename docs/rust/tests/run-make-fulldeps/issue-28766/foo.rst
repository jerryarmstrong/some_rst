tests/run-make-fulldeps/issue-28766/foo.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]
pub struct Foo(());

impl Foo {
  pub fn new() -> Foo {
    Foo(())
  }
}


