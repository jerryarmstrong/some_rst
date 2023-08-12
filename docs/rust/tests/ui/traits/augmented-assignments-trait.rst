tests/ui/traits/augmented-assignments-trait.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
use std::ops::AddAssign;

struct Int(#[allow(unused_tuple_struct_fields)] i32);

impl AddAssign for Int {
    fn add_assign(&mut self, _: Int) {
        unimplemented!()
    }
}

fn main() {}


