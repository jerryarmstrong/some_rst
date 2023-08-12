tests/incremental/static_refering_to_other_static2/issue.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions:rpass1 rpass2

#[cfg(rpass1)]
pub static A: i32 = 42;
#[cfg(rpass2)]
pub static A: i32 = 43;

pub static B: &i32 = &A;

fn main() {}


