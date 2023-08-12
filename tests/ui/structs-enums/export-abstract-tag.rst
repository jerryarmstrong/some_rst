tests/ui/structs-enums/export-abstract-tag.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

// We can export tags without exporting the variants to create a simple
// sort of ADT.

// pretty-expanded FIXME #23616

mod foo {
    pub enum t { t1, }

    pub fn f() -> t { return t::t1; }
}

pub fn main() { let _v: foo::t = foo::f(); }


