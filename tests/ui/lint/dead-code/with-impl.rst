tests/ui/lint/dead-code/with-impl.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![deny(dead_code)]

pub struct GenericFoo<T>(#[allow(unused_tuple_struct_fields)] T);

type Foo = GenericFoo<u32>;

impl Foo {
    fn bar(self) -> u8 {
        0
    }
}

fn main() {
    println!("{}", GenericFoo(0).bar());
}


