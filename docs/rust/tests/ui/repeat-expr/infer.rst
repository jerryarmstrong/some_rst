tests/ui/repeat-expr/infer.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

#[derive(Clone, Default)]
struct MaybeCopy<T>(T);

impl Copy for MaybeCopy<u8> {}

fn is_copy<T: Copy>(x: T) {
    println!("{}", std::any::type_name::<T>());
}

fn main() {
    is_copy(MaybeCopy::default());
    [MaybeCopy::default(); 13];
    // didn't work, because `Copy` was only checked in the mir
}


