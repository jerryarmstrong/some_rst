tests/ui/binding/use-uninit-match.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]


fn foo<T>(o: myoption<T>) -> isize {
    let mut x: isize = 5;
    match o {
        myoption::none::<T> => { }
        myoption::some::<T>(_t) => { x += 1; }
    }
    return x;
}

enum myoption<T> { none, some(T), }

pub fn main() { println!("{}", 5); }


