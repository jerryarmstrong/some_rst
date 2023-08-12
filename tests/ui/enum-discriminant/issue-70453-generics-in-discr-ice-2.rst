tests/ui/enum-discriminant/issue-70453-generics-in-discr-ice-2.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(core_intrinsics)]

extern crate core;
use core::intrinsics::discriminant_value;

#[repr(usize)]
enum MyWeirdOption<T> {
    None = 0,
    Some(T) = std::mem::size_of::<T>(),
    //~^ ERROR generic parameters may not be used in const operations
}

fn main() {
    assert_eq!(discriminant_value(&MyWeirdOption::<u8>::None), 0);
    assert_eq!(discriminant_value(&MyWeirdOption::Some(0u8)), 1);
}


