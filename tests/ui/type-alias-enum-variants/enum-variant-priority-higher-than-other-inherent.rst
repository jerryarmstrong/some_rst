tests/ui/type-alias-enum-variants/enum-variant-priority-higher-than-other-inherent.rs
=====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that an `enum` variant is resolved, in the value namespace,
// with higher priority than other inherent items when there is a conflict.

enum E {
    V(u8)
}

impl E {
    fn V() {}
}

enum E2 {
    V,
}

impl E2 {
    const V: u8 = 0;
}

fn main() {
    <E>::V(); //~ ERROR this enum variant takes 1 argument but 0 arguments were supplied
    let _: u8 = <E2>::V; //~ ERROR mismatched types
}


