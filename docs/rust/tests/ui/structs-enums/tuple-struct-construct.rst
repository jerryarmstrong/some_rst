tests/ui/structs-enums/tuple-struct-construct.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#[allow(unused_tuple_struct_fields)]
#[derive(Debug)]
struct Foo(isize, isize);

pub fn main() {
    let x = Foo(1, 2);
    println!("{:?}", x);
}


