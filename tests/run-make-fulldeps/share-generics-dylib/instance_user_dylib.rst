tests/run-make-fulldeps/share-generics-dylib/instance_user_dylib.rs
===================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate instance_provider_a;
extern crate instance_provider_b;

pub fn foo() {
    instance_provider_a::foo();
    instance_provider_b::foo();
}


