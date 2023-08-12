tests/ui/label/label-static.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    'static: loop { //~ ERROR invalid label name `'static`
        break 'static //~ ERROR invalid label name `'static`
    }
}


