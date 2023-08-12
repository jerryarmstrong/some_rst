tests/ui/type-alias-enum-variants/issue-61801-path-pattern-can-infer.rs
=======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // In this regression test we check that a path pattern referring to a unit variant
// through a type alias is successful in inferring the generic argument.

// check-pass

enum Opt<T> {
    N,
    S(T),
}

type OptAlias<T> = Opt<T>;

fn f1(x: OptAlias<u8>) {
    match x {
        OptAlias::N // We previously failed to infer `T` to `u8`.
            => (),
        _ => (),
    }

    match x {
        <
            OptAlias<_> // And we failed to infer this type also.
        >::N => (),
        _ => (),
    }
}

fn main() {}


