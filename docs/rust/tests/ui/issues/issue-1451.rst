tests/ui/issues/issue-1451.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// pretty-expanded FIXME #23616
#![allow(non_snake_case)]
#![allow(unused_variables)]

struct T { f: extern "Rust" fn() }
struct S { f: extern "Rust" fn() }

fn fooS(t: S) {
}

fn fooT(t: T) {
}

fn bar() {
}

pub fn main() {
    let x: extern "Rust" fn() = bar;
    fooS(S {f: x});
    fooS(S {f: bar});

    let x: extern "Rust" fn() = bar;
    fooT(T {f: x});
    fooT(T {f: bar});
}


