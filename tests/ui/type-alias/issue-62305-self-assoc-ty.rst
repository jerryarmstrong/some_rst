tests/ui/type-alias/issue-62305-self-assoc-ty.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type Alias = Self::Target;
//~^ ERROR failed to resolve: `Self`

fn main() {}


