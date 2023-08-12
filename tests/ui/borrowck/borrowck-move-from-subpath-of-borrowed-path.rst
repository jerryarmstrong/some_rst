tests/ui/borrowck/borrowck-move-from-subpath-of-borrowed-path.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // verify that an error is raised when trying to move out of a
// borrowed path.





fn main() {
    let a: Box<Box<_>> = Box::new(Box::new(2));
    let b = &a;

    let z = *a; //~ ERROR: cannot move out of `*a` because it is borrowed
    b.use_ref();
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


