tests/ui/keyword/extern/keyword-extern-as-identifier-pat.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let extern = 0; //~ ERROR expected identifier, found keyword `extern`
}


