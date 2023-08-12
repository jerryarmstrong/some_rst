tests/ui/pub/pub-restricted-error-fn.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub(crate) () fn foo() {} //~ ERROR visibility `pub(crate)` is not followed by an item
//~^ ERROR expected item, found `(`


