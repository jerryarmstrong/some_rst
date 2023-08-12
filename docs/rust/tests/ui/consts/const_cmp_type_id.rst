tests/ui/consts/const_cmp_type_id.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![feature(const_type_id)]
#![feature(const_trait_impl)]

use std::any::TypeId;

const fn main() {
    assert!(TypeId::of::<u8>() == TypeId::of::<u8>());
    assert!(TypeId::of::<()>() != TypeId::of::<u8>());
    const _A: bool = TypeId::of::<u8>() < TypeId::of::<u16>();
    // can't assert `_A` because it is not deterministic
}


