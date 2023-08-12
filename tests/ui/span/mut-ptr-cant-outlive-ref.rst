tests/ui/span/mut-ptr-cant-outlive-ref.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::RefCell;

fn main() {
    let m = RefCell::new(0);
    let p;
    {
        let b = m.borrow();
        p = &*b;
    }
    //~^^ ERROR `b` does not live long enough
    p.use_ref();
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


