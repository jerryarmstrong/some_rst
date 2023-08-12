src/tools/clippy/tests/ui/crashes/inherent_impl.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(clippy::multiple_inherent_impl)]

/// Test for https://github.com/rust-lang/rust-clippy/issues/4578

macro_rules! impl_foo {
    ($struct:ident) => {
        impl $struct {
            fn foo() {}
        }
    };
}

macro_rules! impl_bar {
    ($struct:ident) => {
        impl $struct {
            fn bar() {}
        }
    };
}

struct MyStruct;

impl_foo!(MyStruct);
impl_bar!(MyStruct);

fn main() {}


