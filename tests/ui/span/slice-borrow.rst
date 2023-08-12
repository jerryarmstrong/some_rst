tests/ui/span/slice-borrow.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test slicing expressions doesn't defeat the borrow checker.

fn main() {
    let y;
    {
        let x: &[isize] = &vec![1, 2, 3, 4, 5];
        //~^ ERROR temporary value dropped while borrowed
        y = &x[1..];
    }
    y.use_ref();
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


