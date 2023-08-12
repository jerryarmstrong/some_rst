tests/ui/inference/need_type_info/do-not-suggest-generic-arguments-for-turbofish.rs
===================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum OhNo<T, U> {
    A(T),
    B(U),
    C,
}

fn uwu() {
    OhNo::C::<u32, _>; //~ ERROR type annotations needed
}

fn main() {}


