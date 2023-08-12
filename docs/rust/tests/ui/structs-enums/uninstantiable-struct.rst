tests/ui/structs-enums/uninstantiable-struct.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
pub struct Z(#[allow(unused_tuple_struct_fields)] &'static Z);

pub fn main() {}


