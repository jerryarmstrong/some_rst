src/tools/miri/tests/pass/extern_types.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(extern_types)]

extern "C" {
    type Foo;
}

fn main() {
    let x: &Foo = unsafe { &*(16 as *const Foo) };
    let _y: &Foo = &*x;
}


