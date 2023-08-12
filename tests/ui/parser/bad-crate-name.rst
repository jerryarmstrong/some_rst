tests/ui/parser/bad-crate-name.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate krate-name-here;
//~^ ERROR crate name using dashes are not valid in `extern crate` statements
//~| ERROR can't find crate for `krate_name_here`

fn main() {}


