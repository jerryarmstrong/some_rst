tests/ui/binding/use-uninit-match2.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(unused_mut)]
#![allow(non_camel_case_types)]


fn foo<T>(o: myoption<T>) -> isize {
    let mut x: isize;
    match o {
        myoption::none::<T> => { panic!(); }
        myoption::some::<T>(_t) => { x = 5; }
    }
    return x;
}

enum myoption<T> { none, some(T), }

pub fn main() { println!("{}", 5); }


