tests/ui/type/type-arg-out-of-scope.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:can't use generic parameters from outer function
fn foo<T>(x: T) {
    fn bar(f: Box<dyn FnMut(T) -> T>) { }
}
fn main() { foo(1); }


