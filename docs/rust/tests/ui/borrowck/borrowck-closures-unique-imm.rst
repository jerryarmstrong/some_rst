tests/ui/borrowck/borrowck-closures-unique-imm.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    x: isize,
}

pub fn main() {
    let mut this = &mut Foo {
        x: 1,
    };
    let mut r = || {
        let p = &this.x;
        &mut this.x; //~ ERROR cannot borrow
        p.use_ref();
    };
    r()
}

trait Fake { fn use_mut(&mut self) { } fn use_ref(&self) { }  }
impl<T> Fake for T { }


