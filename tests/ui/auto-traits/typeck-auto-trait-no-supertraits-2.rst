tests/ui/auto-traits/typeck-auto-trait-no-supertraits-2.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(auto_traits)]
#![feature(negative_impls)]

auto trait Magic : Sized where Option<Self> : Magic {} //~ ERROR E0568
//~^ ERROR E0568
impl<T:Magic> Magic for T {}

fn copy<T: Magic>(x: T) -> (T, T) { (x, x) }

#[derive(Debug)]
struct NoClone;

fn main() {
    let (a, b) = copy(NoClone);
    println!("{:?} {:?}", a, b);
}


