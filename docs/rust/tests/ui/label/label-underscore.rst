tests/ui/label/label-underscore.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    '_: loop { //~ ERROR invalid label name `'_`
        break '_ //~ ERROR invalid label name `'_`
    }
}


