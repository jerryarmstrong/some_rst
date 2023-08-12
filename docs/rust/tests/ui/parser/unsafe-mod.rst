tests/ui/parser/unsafe-mod.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    unsafe mod m {
    //~^ ERROR module cannot be declared unsafe
}

unsafe mod n;
//~^ ERROR module cannot be declared unsafe
//~^^ ERROR file not found for module `n`

fn main() {}


