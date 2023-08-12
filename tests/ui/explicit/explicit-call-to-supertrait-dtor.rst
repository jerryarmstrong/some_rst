tests/ui/explicit/explicit-call-to-supertrait-dtor.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
struct Foo {
    x: isize
}

#[allow(drop_bounds)]
trait Bar: Drop {
    fn blah(&self);
}

impl Drop for Foo {
    fn drop(&mut self) {
        println!("kaboom");
    }
}

impl Bar for Foo {
    fn blah(&self) {
        self.drop();    //~ ERROR explicit use of destructor method
    }
}

fn main() {
    let x = Foo { x: 3 };
    println!("{}", x.x);
}


