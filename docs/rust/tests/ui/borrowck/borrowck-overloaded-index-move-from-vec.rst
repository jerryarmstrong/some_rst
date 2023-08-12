tests/ui/borrowck/borrowck-overloaded-index-move-from-vec.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::Index;

struct MyVec<T> {
    data: Vec<T>,
}

impl<T> Index<usize> for MyVec<T> {
    type Output = T;

    fn index(&self, i: usize) -> &T {
        &self.data[i]
    }
}



fn main() {
    let v = MyVec::<Box<_>> { data: vec![Box::new(1), Box::new(2), Box::new(3)] };
    let good = &v[0]; // Shouldn't fail here
    let bad = v[0];
    //~^ ERROR cannot move out of index of `MyVec<Box<i32>>`
}


