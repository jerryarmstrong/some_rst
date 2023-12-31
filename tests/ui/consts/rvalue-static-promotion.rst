tests/ui/consts/rvalue-static-promotion.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::cell::Cell;

const NONE_CELL_STRING: Option<Cell<String>> = None;

struct Foo<T>(#[allow(unused_tuple_struct_fields)] T);
impl<T> Foo<T> {
    const FOO: Option<Box<T>> = None;
}

fn main() {
    let _: &'static u32 = &42;
    let _: &'static Option<u32> = &None;

    // We should be able to peek at consts and see they're None.
    let _: &'static Option<Cell<String>> = &NONE_CELL_STRING;
    let _: &'static Option<Box<()>> = &Foo::FOO;
}


