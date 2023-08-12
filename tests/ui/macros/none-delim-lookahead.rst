tests/ui/macros/none-delim-lookahead.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

macro_rules! make_struct {
    ($name:ident) => {
        #[derive(Debug)]
        struct Foo {
            #[cfg(not(FALSE))]
            field: fn($name: bool)
        }
    }
}

make_struct!(param_name);

fn main() {}


