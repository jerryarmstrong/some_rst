tests/ui/deprecation/deprecated_no_stack_check.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(warnings)]
#![feature(no_stack_check)]
//~^ ERROR: feature has been removed [E0557]
fn main() {

}


