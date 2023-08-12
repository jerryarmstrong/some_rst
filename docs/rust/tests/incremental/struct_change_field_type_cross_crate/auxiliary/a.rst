tests/incremental/struct_change_field_type_cross_crate/auxiliary/a.rs
=====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="rlib"]

 #[cfg(rpass1)]
pub struct X {
    pub x: u32
}

#[cfg(rpass2)]
pub struct X {
    pub x: i32
}

pub struct EmbedX {
    pub x: X
}

pub struct Y {
    pub y: char
}


