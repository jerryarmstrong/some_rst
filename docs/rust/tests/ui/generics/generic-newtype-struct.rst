tests/ui/generics/generic-newtype-struct.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

struct S<T>(#[allow(unused_tuple_struct_fields)] T);

pub fn main() {
    let _s = S(2);
}


