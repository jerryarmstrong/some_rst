tests/ui/generics/generic-ivec-leak.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]
enum wrapper<T> { wrapped(#[allow(unused_tuple_struct_fields)] T), }

pub fn main() { let _w = wrapper::wrapped(vec![1, 2, 3, 4, 5]); }


