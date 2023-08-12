tests/ui/traits/inductive-overflow/supertrait-auto-trait.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Auto-trait-based version of #29859, supertrait version. Test that using
// a simple auto trait `..` impl alone still doesn't allow arbitrary bounds
// to be synthesized.

#![feature(auto_traits)]
#![feature(negative_impls)]

auto trait Magic: Copy {} //~ ERROR E0568

fn copy<T: Magic>(x: T) -> (T, T) { (x, x) }

#[derive(Debug)]
struct NoClone;

fn main() {
    let (a, b) = copy(NoClone); //~ ERROR
    println!("{:?} {:?}", a, b);
}


