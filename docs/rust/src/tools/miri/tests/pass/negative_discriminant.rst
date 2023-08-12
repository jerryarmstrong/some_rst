src/tools/miri/tests/pass/negative_discriminant.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum AB {
    A = -1,
    B = 1,
}

fn main() {
    match AB::A {
        AB::A => (),
        AB::B => panic!(),
    }

    match AB::B {
        AB::A => panic!(),
        AB::B => (),
    }
}


