tests/ui/conditional-compilation/cfg_accessible-unstable.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg_accessible(std)] //~ ERROR use of unstable library feature 'cfg_accessible'
fn main() {}


