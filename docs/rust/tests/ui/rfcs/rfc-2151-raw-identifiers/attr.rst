tests/ui/rfcs/rfc-2151-raw-identifiers/attr.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::mem;

#[r#repr(r#C, r#packed)]
struct Test {
    a: bool, b: u64
}

#[r#derive(r#Debug)]
struct Test2(#[allow(unused_tuple_struct_fields)] u32);

pub fn main() {
    assert_eq!(mem::size_of::<Test>(), 9);
    assert_eq!("Test2(123)", format!("{:?}", Test2(123)));
}


