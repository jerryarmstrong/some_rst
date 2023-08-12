tests/ui/deriving/deriving-clone-generic-struct.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

#![allow(dead_code)]

#[derive(Clone)]
struct S<T> {
    foo: (),
    bar: (),
    baz: T,
}

pub fn main() {
    let _ = S { foo: (), bar: (), baz: 1 }.clone();
}


