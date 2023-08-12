tests/ui/issues/auxiliary/issue-48984-aux.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]
#![crate_name = "issue48984aux"]

pub trait Foo { type Item; }

pub trait Bar: Foo<Item=[u8;1]> {  }


