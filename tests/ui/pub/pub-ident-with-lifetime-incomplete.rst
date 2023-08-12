tests/ui/pub/pub-ident-with-lifetime-incomplete.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
}

pub   foo<'a>
//~^ ERROR missing `fn` or `struct` for function or struct definition


