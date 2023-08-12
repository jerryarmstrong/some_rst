tests/ui/resolve/resolve-issue-2428.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(non_camel_case_types)]
#![allow(non_upper_case_globals)]

const foo: isize = 4 >> 1;
enum bs { thing = foo }
pub fn main() { assert_eq!(bs::thing as isize, foo); }


