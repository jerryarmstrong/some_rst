tests/ui/generics/generic-tag-values.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_camel_case_types)]

enum noption<T> { some(T), }

struct Pair { x: isize, y: isize }

pub fn main() {
    let nop: noption<isize> = noption::some::<isize>(5);
    match nop { noption::some::<isize>(n) => { println!("{}", n); assert_eq!(n, 5); } }
    let nop2: noption<Pair> = noption::some(Pair{x: 17, y: 42});
    match nop2 {
      noption::some(t) => {
        println!("{}", t.x);
        println!("{}", t.y);
        assert_eq!(t.x, 17);
        assert_eq!(t.y, 42);
      }
    }
}


