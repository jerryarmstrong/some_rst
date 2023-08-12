tests/ui/wf/wf-const-type.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we check the types of constants are well-formed.

#![feature(associated_type_defaults)]

#![allow(dead_code)]

struct IsCopy<T:Copy> { t: T }
struct NotCopy;

const FOO: IsCopy<Option<NotCopy>> = IsCopy { t: None };
//~^ ERROR E0277


fn main() { }


