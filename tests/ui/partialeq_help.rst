tests/ui/partialeq_help.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T: PartialEq>(a: &T, b: T) {
    a == b; //~ ERROR E0277
}

fn foo2<T: PartialEq>(a: &T, b: T) where {
    a == b; //~ ERROR E0277
}

fn main() {
    foo(&1, 1);
    foo2(&1, 1);
}


