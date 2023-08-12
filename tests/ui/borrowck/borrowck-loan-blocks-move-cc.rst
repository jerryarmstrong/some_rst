tests/ui/borrowck/borrowck-loan-blocks-move-cc.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::thread;



fn borrow<F>(v: &isize, f: F) where F: FnOnce(&isize) {
    f(v);
}



fn box_imm() {
    let v: Box<_> = Box::new(3);
    let w = &v;
    thread::spawn(move|| {
    //~^ ERROR cannot move out of `v` because it is borrowed
        println!("v={}", *v);
    });
    w.use_ref();
}

fn box_imm_explicit() {
    let v: Box<_> = Box::new(3);
    let w = &v;
    thread::spawn(move|| {
    //~^ ERROR cannot move
        println!("v={}", *v);
    });
    w.use_ref();
}

fn main() {
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


