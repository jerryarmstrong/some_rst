tests/ui/borrowck/borrowck-issue-2657-1.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


fn main() {
    let x: Option<Box<_>> = Some(Box::new(1));
    match x {
      Some(ref _y) => {
        let _a = x; //~ ERROR cannot move
        _y.use_ref();
      }
      _ => {}
    }
}


