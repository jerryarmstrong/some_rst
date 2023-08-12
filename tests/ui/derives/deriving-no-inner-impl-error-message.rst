tests/ui/derives/deriving-no-inner-impl-error-message.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct NoCloneOrEq;

#[derive(PartialEq)]
struct E {
    x: NoCloneOrEq //~ ERROR binary operation `==` cannot be applied to type `NoCloneOrEq`
}
#[derive(Clone)]
struct C {
    x: NoCloneOrEq
    //~^ ERROR `NoCloneOrEq: Clone` is not satisfied
}


fn main() {}


