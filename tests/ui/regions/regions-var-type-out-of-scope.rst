tests/ui/regions/regions-var-type-out-of-scope.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn id<T>(x: T) -> T { x }

fn foo(cond: bool) {
    // Here we will infer a type that uses the
    // region of the if stmt then block:
    let mut x;

    if cond {
        x = &id(3); //~ ERROR temporary value dropped while borrowed
        assert_eq!(*x, 3);
    }
}

fn main() {}


