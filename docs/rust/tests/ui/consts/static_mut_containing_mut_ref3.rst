tests/ui/consts/static_mut_containing_mut_ref3.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    static mut FOO: (u8, u8) = (42, 43);

static mut BAR: () = unsafe { FOO.0 = 99; };
//~^ ERROR could not evaluate static initializer

fn main() {}


