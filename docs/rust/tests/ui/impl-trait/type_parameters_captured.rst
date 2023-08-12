tests/ui/impl-trait/type_parameters_captured.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::fmt::Debug;

trait Any {}
impl<T> Any for T {}

// Check that type parameters are captured and not considered 'static
fn foo<T>(x: T) -> impl Any + 'static {
    x
    //~^ ERROR the parameter type `T` may not live long enough
}

fn main() {}


