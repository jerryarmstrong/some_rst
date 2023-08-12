tests/ui/const-generics/incorrect-number-of-const-args.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<const X: usize, const Y: usize>() -> usize {
    0
}

fn main() {
    foo::<0>();
    //~^ ERROR function takes 2

    foo::<0, 0, 0>();
    //~^ ERROR function takes 2
}


