src/tools/miri/tests/pass/small_enum_size_bug.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(dead_code)]
enum E {
    A = 1,
    B = 2,
    C = 3,
}

fn main() {
    let enone = None::<E>;
    if let Some(..) = enone {
        panic!();
    }
}


