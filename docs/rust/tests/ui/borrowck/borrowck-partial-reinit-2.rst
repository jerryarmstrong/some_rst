tests/ui/borrowck/borrowck-partial-reinit-2.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Test {
    a: isize,
    b: Option<Box<Test>>,
}

impl Drop for Test {
    fn drop(&mut self) {
        println!("Dropping {}", self.a);
    }
}

fn stuff() {
    let mut t = Test { a: 1, b: None};
    let mut u = Test { a: 2, b: Some(Box::new(t))};
    t.b = Some(Box::new(u));
    //~^ ERROR assign of moved value: `t`
    println!("done");
}

fn main() {
    stuff();
    println!("Hello, world!")
}


