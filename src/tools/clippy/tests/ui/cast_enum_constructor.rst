src/tools/clippy/tests/ui/cast_enum_constructor.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::cast_enum_constructor)]
#![allow(clippy::fn_to_numeric_cast)]

fn main() {
    enum Foo {
        Y(u32),
    }

    enum Bar {
        X,
    }

    let _ = Foo::Y as usize;
    let _ = Foo::Y as isize;
    let _ = Foo::Y as fn(u32) -> Foo;
    let _ = Bar::X as usize;
}


