tests/ui/keyword/extern/keyword-extern-as-identifier-expr.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let s = extern::foo::Bar; //~ ERROR expected expression, found keyword `extern`
}


