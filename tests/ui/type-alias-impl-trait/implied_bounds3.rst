tests/ui/type-alias-impl-trait/implied_bounds3.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn foo<F>(_: F)
where
    F: 'static,
{
}

fn from<F: Send>(f: F) -> impl Send {
    f
}

fn bar<T>() {
    foo(from(|| ()))
}

fn main() {
}


