tests/ui/suggestions/suggest-assoc-fn-call-with-turbofish-placeholder.rs
========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct GenericAssocMethod<T>(T);

impl<T> GenericAssocMethod<T> {
    fn default_hello() {}
}

fn main() {
    let x = GenericAssocMethod(33);
    x.default_hello();
    //~^ ERROR no method named `default_hello` found
}


