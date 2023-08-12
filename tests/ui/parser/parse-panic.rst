tests/ui/parser/parse-panic.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]
#![allow(unreachable_code)]

fn dont_call_me() { panic!(); println!("{}", 1); }

pub fn main() { }


