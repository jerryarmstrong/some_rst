tests/ui/unique-object-noncopyable.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Foo {
    fn f(&self);
}

struct Bar {
    x: isize,
}

impl Drop for Bar {
    fn drop(&mut self) {}
}

impl Foo for Bar {
    fn f(&self) {
        println!("hi");
    }
}



fn main() {
    let x = Box::new(Bar { x: 10 });
    let y: Box<dyn Foo> = x as Box<dyn Foo>;
    let _z = y.clone(); //~ ERROR the method
}


