tests/ui/lint/trivial-casts.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(trivial_casts, trivial_numeric_casts)]

fn main() {
    let lugubrious = 12i32 as i32;
    //~^ ERROR trivial numeric cast
    let haunted: &u32 = &99;
    let _ = haunted as *const u32;
    //~^ ERROR trivial cast
}


