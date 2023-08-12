tests/run-make-fulldeps/issue-28766/main.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]
extern crate foo;
use foo::Foo;

pub fn crash() -> Box<Foo> {
  Box::new(Foo::new())
}


