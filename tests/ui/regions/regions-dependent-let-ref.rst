tests/ui/regions/regions-dependent-let-ref.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test lifetimes are linked properly when we take reference
// to interior.

// pretty-expanded FIXME #23616

struct Foo(isize);
pub fn main() {
    // Here the lifetime of the `&` should be at least the
    // block, since a ref binding is created to the interior.
    let &Foo(ref _x) = &Foo(3);
}


