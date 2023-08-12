src/tools/rustfmt/tests/source/nested-if-else.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn issue1518() {
    Some(Object {
        field: if a {
            a_thing
        } else if b {
            b_thing
        } else {
            c_thing
        },
    })
}


