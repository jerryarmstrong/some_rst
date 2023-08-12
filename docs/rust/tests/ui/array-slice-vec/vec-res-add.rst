tests/ui/array-slice-vec/vec-res-add.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Debug)]
struct R {
  i:isize
}

fn r(i:isize) -> R { R { i: i } }

impl Drop for R {
    fn drop(&mut self) {}
}

fn main() {
    // This can't make sense as it would copy the classes
    let i = vec![r(0)];
    let j = vec![r(1)];
    let k = i + j;
    //~^ ERROR cannot add `Vec<R>` to `Vec<R>`
    println!("{:?}", j);
}


