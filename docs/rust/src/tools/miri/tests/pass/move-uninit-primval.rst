src/tools/miri/tests/pass/move-uninit-primval.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(deprecated)]

use std::mem;

struct Foo {
    _inner: mem::MaybeUninit<i32>,
}

fn main() {
    unsafe {
        let foo = Foo { _inner: mem::uninitialized() };
        let _bar = foo;
    }
}


