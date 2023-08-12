tests/ui/copy-a-resource.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Debug)]
struct Foo {
  i: isize,
}

impl Drop for Foo {
    fn drop(&mut self) {}
}

fn foo(i:isize) -> Foo {
    Foo {
        i: i
    }
}

fn main() {
    let x = foo(10);
    let _y = x.clone();
    //~^ ERROR no method named `clone` found
    println!("{:?}", x);
}


