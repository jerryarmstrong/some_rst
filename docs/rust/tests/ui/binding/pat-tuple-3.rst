tests/ui/binding/pat-tuple-3.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn tuple() {
    let x = (1, 2, 3);
    let branch = match x {
        (1, 1, ..) => 0,
        (1, 2, 3, ..) => 1,
        (1, 2, ..) => 2,
        _ => 3
    };
    assert_eq!(branch, 1);
}

fn tuple_struct() {
    struct S(u8, u8, u8);

    let x = S(1, 2, 3);
    let branch = match x {
        S(1, 1, ..) => 0,
        S(1, 2, 3, ..) => 1,
        S(1, 2, ..) => 2,
        _ => 3
    };
    assert_eq!(branch, 1);
}

fn main() {
    tuple();
    tuple_struct();
}


