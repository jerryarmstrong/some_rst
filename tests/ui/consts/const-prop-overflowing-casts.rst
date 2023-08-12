tests/ui/consts/const-prop-overflowing-casts.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

enum Foo {
    Bar = -42,
    Baz = 42,
}

fn main() {
    let _ = 0u8 as u32;
    let _ = (1u32 << 31) as u16;
    let _ = (1u16 << 15) as u8;
    let _ = (!0u16) as u8;
    let _ = (-1i16) as i8;
    let _ = (Foo::Bar) as i8;
}


