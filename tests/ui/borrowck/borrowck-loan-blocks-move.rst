tests/ui/borrowck/borrowck-loan-blocks-move.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn take(_v: Box<isize>) {
}





fn box_imm() {
    let v = Box::new(3);
    let w = &v;
    take(v); //~ ERROR cannot move out of `v` because it is borrowed
    w.use_ref();
}

fn main() {
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


