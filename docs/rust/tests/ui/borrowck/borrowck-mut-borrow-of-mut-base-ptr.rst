tests/ui/borrowck/borrowck-mut-borrow-of-mut-base-ptr.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that attempt to mutably borrow `&mut` pointer while pointee is
// borrowed yields an error.
//
// Example from compiler/rustc_borrowck/borrowck/README.md



fn foo<'a>(mut t0: &'a mut isize,
           mut t1: &'a mut isize) {
    let p: &isize = &*t0;     // Freezes `*t0`
    let mut t2 = &mut t0;   //~ ERROR cannot borrow `t0`
    **t2 += 1;              // Mutates `*t0`
    p.use_ref();
}

fn bar<'a>(mut t0: &'a mut isize,
           mut t1: &'a mut isize) {
    let p: &mut isize = &mut *t0; // Claims `*t0`
    let mut t2 = &mut t0;       //~ ERROR cannot borrow `t0`
    **t2 += 1;                  // Mutates `*t0` but not through `*p`
    p.use_mut();
}

fn main() {
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


