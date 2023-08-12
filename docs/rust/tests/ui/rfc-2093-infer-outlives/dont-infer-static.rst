tests/ui/rfc-2093-infer-outlives/dont-infer-static.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /*
 * We don't infer `T: 'static` outlives relationships.
 */

struct Foo<U> {
    bar: Bar<U> //~ ERROR the parameter type `U` may not live long enough [E0310]
}
struct Bar<T: 'static> {
    x: T,
}

fn main() {}


