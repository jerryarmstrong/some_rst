tests/ui/binding/pat-tuple-2.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
fn tuple() {
    let x = (1,);
    match x {
        (2, ..) => panic!(),
        (..) => ()
    }
}

fn tuple_struct() {
    struct S(u8);

    let x = S(1);
    match x {
        S(2, ..) => panic!(),
        S(..) => ()
    }
}

fn main() {
    tuple();
    tuple_struct();
}


