tests/ui/traits/issue-7013.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::cell::RefCell;
use std::rc::Rc;

trait Foo {
    fn set(&mut self, v: Rc<RefCell<A>>);
}

struct B {
    v: Option<Rc<RefCell<A>>>
}

impl Foo for B {
    fn set(&mut self, v: Rc<RefCell<A>>)
    {
        self.v = Some(v);
    }
}

struct A {
    v: Box<dyn Foo + Send>,
}

fn main() {
    let a = A {v: Box::new(B{v: None}) as Box<dyn Foo + Send>};
    //~^ ERROR `Rc<RefCell<A>>` cannot be sent between threads safely
}


