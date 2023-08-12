tests/ui/traits/impl-for-module.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
}

trait A {
}

impl A for a { //~ ERROR expected type, found module
}

fn main() {
}


