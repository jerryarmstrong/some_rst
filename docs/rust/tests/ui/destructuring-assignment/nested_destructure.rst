tests/ui/destructuring-assignment/nested_destructure.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Struct<S, T> {
    a: S,
    b: T,
}

struct TupleStruct<S, T>(S, T);

fn main() {
    let (a, b, c, d);
    Struct { a: TupleStruct((a, b), c), b: [d] } =
        Struct { a: TupleStruct((0, 1), 2), b: [3] };
    assert_eq!((a, b, c, d), (0, 1, 2, 3));

    // unnested underscore: just discard
    _ = 1;
}


