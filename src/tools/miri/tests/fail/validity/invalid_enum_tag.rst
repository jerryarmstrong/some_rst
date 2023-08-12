src/tools/miri/tests/fail/validity/invalid_enum_tag.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr(C)]
pub enum Foo {
    A,
    B,
    C,
    D,
}

fn main() {
    let _f = unsafe { std::mem::transmute::<i32, Foo>(42) }; //~ ERROR: constructing invalid value at .<enum-tag>: encountered 0x0000002a, but expected a valid enum tag
}


