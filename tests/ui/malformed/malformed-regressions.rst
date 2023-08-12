tests/ui/malformed/malformed-regressions.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc] //~ ERROR attribute must be of the form
//~^ WARN this was previously accepted
#[ignore()] //~ ERROR attribute must be of the form
//~^ WARN this was previously accepted
#[inline = ""] //~ ERROR attribute must be of the form
//~^ WARN this was previously accepted
#[link] //~ ERROR attribute must be of the form
//~^ WARN this was previously accepted
#[link = ""] //~ ERROR attribute must be of the form
//~^ WARN this was previously accepted

fn main() {}


