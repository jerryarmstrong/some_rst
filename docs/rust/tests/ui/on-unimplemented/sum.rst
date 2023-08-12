tests/ui/on-unimplemented/sum.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // <https://github.com/rust-lang/rust/issues/105184>

fn main() {
    vec![(), ()].iter().sum::<i32>();
    //~^ ERROR

    vec![(), ()].iter().product::<i32>();
    //~^ ERROR
}


