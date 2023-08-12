tests/ui/generics/generic-recursive-tag.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

enum list<T> { #[allow(unused_tuple_struct_fields)] cons(Box<T>, Box<list<T>>), nil, }

pub fn main() {
    let _a: list<isize> =
        list::cons::<isize>(Box::new(10),
        Box::new(list::cons::<isize>(Box::new(12),
        Box::new(list::cons::<isize>(Box::new(13),
        Box::new(list::nil::<isize>))))));
}


