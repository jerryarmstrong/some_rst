tests/ui/consts/self_normalization.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn testfn(_arr: &mut [(); 0]) {}

trait TestTrait {
    fn method();
}

impl TestTrait for [(); 0] {
    fn method() {
        let mut arr: Self = [(); 0];
        testfn(&mut arr);
    }
}

fn main() {}


