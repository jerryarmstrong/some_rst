tests/ui/type-alias-enum-variants/resolve-to-enum-variant-in-type-namespace-and-error.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that the compiler will resolve `<E>::V` to the variant `V` in the type namespace
// but will reject this because `enum` variants do not exist in the type namespace.

enum E {
    V
}

fn check() -> <E>::V {}
//~^ ERROR expected type, found variant `V`

fn main() {}


