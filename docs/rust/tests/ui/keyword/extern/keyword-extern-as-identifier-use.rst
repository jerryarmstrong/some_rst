tests/ui/keyword/extern/keyword-extern-as-identifier-use.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use extern::foo; //~ ERROR expected identifier, found keyword `extern`
                 //~| ERROR unresolved import `r#extern`

fn main() {}


