tests/ui/macros/macro-attribute.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[doc = $not_there] //~ ERROR expected expression, found `$`
fn main() { }


