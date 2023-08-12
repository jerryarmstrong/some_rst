tests/ui/resolve/crate-called-as-function.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    ::foo() //~ cannot find external crate `foo` in the crate root
}


