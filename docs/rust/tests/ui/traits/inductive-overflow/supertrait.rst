tests/ui/traits/inductive-overflow/supertrait.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for #29859, supertrait version. This example
// allowed arbitrary trait bounds to be synthesized.

trait Magic: Copy {}
impl<T: Magic> Magic for T {}

fn copy<T: Magic>(x: T) -> (T, T) { (x, x) }

#[derive(Debug)]
struct NoClone;

fn main() {
    let (a, b) = copy(NoClone); //~ ERROR E0275
    println!("{:?} {:?}", a, b);
}


