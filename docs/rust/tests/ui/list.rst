tests/ui/list.rs
================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_camel_case_types)]
// pretty-expanded FIXME #23616

enum list { #[allow(unused_tuple_struct_fields)] cons(isize, Box<list>), nil, }

pub fn main() {
    list::cons(10, Box::new(list::cons(11, Box::new(list::cons(12, Box::new(list::nil))))));
}


