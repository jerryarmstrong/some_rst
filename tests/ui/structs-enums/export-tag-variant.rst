tests/ui/structs-enums/export-tag-variant.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]
// pretty-expanded FIXME #23616

mod foo {
    pub enum t { t1, }
}

pub fn main() { let _v = foo::t::t1; }


