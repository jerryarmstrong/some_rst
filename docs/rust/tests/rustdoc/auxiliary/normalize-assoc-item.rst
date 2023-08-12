tests/rustdoc/auxiliary/normalize-assoc-item.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name = "inner"]
pub trait MyTrait {
    type Y;
}

impl MyTrait for u32 {
    type Y = i32;
}

pub fn foo() -> <u32 as MyTrait>::Y {
    0
}


