tests/ui/explicit/explicit-call-to-dtor.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix
struct Foo {
    x: isize
}

impl Drop for Foo {
    fn drop(&mut self) {
        println!("kaboom");
    }
}

fn main() {
    let x = Foo { x: 3 };
    println!("{}", x.x);
    x.drop();   //~ ERROR explicit use of destructor method
}


