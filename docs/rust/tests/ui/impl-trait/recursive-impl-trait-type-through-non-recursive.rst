tests/ui/impl-trait/recursive-impl-trait-type-through-non-recursive.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that impl trait does not allow creating recursive types that are
// otherwise forbidden. Even when there's an opaque type in another crate
// hiding this.

fn id<T>(t: T) -> impl Sized { t }

fn recursive_id() -> impl Sized { //~ ERROR cannot resolve opaque type
    id(recursive_id2())
}

fn recursive_id2() -> impl Sized { //~ ERROR cannot resolve opaque type
    id(recursive_id())
}

fn wrap<T>(t: T) -> impl Sized { (t,) }

fn recursive_wrap() -> impl Sized { //~ ERROR cannot resolve opaque type
    wrap(recursive_wrap2())
}

fn recursive_wrap2() -> impl Sized { //~ ERROR cannot resolve opaque type
    wrap(recursive_wrap())
}

fn main() {}


