tests/ui/const-generics/unused-type-param-suggestion.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type="lib"]

struct Example<N>;
//~^ ERROR parameter


