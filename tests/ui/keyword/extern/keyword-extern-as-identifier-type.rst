tests/ui/keyword/extern/keyword-extern-as-identifier-type.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    type A = extern::foo::bar; //~ ERROR expected type, found keyword `extern`

fn main() {}


