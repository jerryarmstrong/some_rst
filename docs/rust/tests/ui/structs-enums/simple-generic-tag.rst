tests/ui/structs-enums/simple-generic-tag.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]



// pretty-expanded FIXME #23616

enum clam<T> { a(T), }

pub fn main() { }


