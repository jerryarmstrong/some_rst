tests/ui/issues/auxiliary/issue-3979-traits.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_name="issue_3979_traits"]

#![crate_type = "lib"]

pub trait Positioned {
  fn SetX(&mut self, _: isize);
  fn X(&self) -> isize;
}

pub trait Movable: Positioned {
  fn translate(&mut self, dx: isize) {
    let x = self.X() + dx;
    self.SetX(x);
  }
}


