tests/ui/mutual-recursion-group.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_camel_case_types)]
#![allow(dead_code)]

// pretty-expanded FIXME #23616

enum colour { red, green, blue, }

enum tree { children(Box<list>), leaf(colour), }

enum list { cons(Box<tree>, Box<list>), nil, }

enum small_list { kons(isize, Box<small_list>), neel, }

pub fn main() { }


