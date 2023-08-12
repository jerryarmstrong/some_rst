tests/ui/pub/pub-ident-fn-or-struct.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub S (foo) bar
//~^ ERROR missing `fn` or `struct` for function or struct definition

fn main() {}


