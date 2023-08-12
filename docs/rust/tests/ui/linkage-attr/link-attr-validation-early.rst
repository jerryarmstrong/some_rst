tests/ui/linkage-attr/link-attr-validation-early.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Top-level ill-formed
#[link] //~ ERROR attribute must be of the form
        //~| WARN this was previously accepted
#[link = "foo"] //~ ERROR attribute must be of the form
                //~| WARN this was previously accepted
extern "C" {}

fn main() {}


