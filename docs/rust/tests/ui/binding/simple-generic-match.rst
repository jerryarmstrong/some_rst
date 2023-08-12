tests/ui/binding/simple-generic-match.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

enum clam<T> { a(#[allow(unused_tuple_struct_fields)] T), }

pub fn main() { let c = clam::a(2); match c { clam::a::<isize>(_) => { } } }


