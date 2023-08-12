tests/ui/array-slice-vec/show-boxed-slice.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[derive(Debug)]
struct Foo(#[allow(unused_tuple_struct_fields)] Box<[u8]>);

pub fn main() {
    println!("{:?}", Foo(Box::new([0, 1, 2])));
}


