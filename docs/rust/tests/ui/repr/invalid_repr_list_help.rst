tests/ui/repr/invalid_repr_list_help.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[repr(uwu)] //~ERROR: unrecognized representation hint
pub struct OwO;

#[repr(uwu = "a")] //~ERROR: unrecognized representation hint
pub struct OwO2(i32);

#[repr(uwu(4))] //~ERROR: unrecognized representation hint
pub struct OwO3 {
    x: i32,
}

#[repr(uwu, u8)] //~ERROR: unrecognized representation hint
pub enum OwO4 {
    UwU = 1,
}


