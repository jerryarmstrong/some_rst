tests/ui/regions/regions-nullary-variant.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

enum roption<'a> {
    a, b(&'a usize)
}

fn mk(cond: bool, ptr: &usize) -> roption {
    if cond {roption::a} else {roption::b(ptr)}
}

pub fn main() {}


