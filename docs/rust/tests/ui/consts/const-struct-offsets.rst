tests/ui/consts/const-struct-offsets.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616
#![allow(non_upper_case_globals)]

enum Foo {
    IntVal(i32),
    Int64Val(i64)
}

struct Bar {
    i: i32,
    v: Foo
}

static bar: Bar = Bar { i: 0, v: Foo::IntVal(0) };

pub fn main() {}


