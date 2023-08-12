tests/ui/resolve/bad-type-env-capture.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T>() {
    fn bar(b: T) { } //~ ERROR can't use generic parameters from outer
}
fn main() { }


