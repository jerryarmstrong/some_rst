tests/ui/structs/rhs-type.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that codegen treats the rhs of pth's decl
// as a _|_-typed thing, not a str-typed thing

// run-fail
// error-pattern:bye
// ignore-emscripten no processes

#![allow(unreachable_code)]
#![allow(unused_variables)]

struct T {
    t: String,
}

fn main() {
    let pth = panic!("bye");
    let _rs: T = T { t: pth };
}


