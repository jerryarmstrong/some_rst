tests/ui/rustdoc/doc_keyword.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![feature(rustdoc_internals)]

#![doc(keyword = "hello")] //~ ERROR

#[doc(keyword = "hell")] //~ ERROR
mod foo {
    fn hell() {}
}

#[doc(keyword = "hall")] //~ ERROR
fn foo() {}


// Regression test for the ICE described in #83512.
trait Foo {
    #[doc(keyword = "match")]
    //~^ ERROR: `#[doc(keyword = "...")]` should be used on modules
    fn quux() {}
}


