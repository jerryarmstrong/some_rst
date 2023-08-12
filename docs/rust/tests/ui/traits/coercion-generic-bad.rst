tests/ui/traits/coercion-generic-bad.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Struct {
    person: &'static str
}

trait Trait<T> {
    fn f(&self, x: T);
}

impl Trait<&'static str> for Struct {
    fn f(&self, x: &'static str) {
        println!("Hello, {}!", x);
    }
}

fn main() {
    let s: Box<dyn Trait<isize>> = Box::new(Struct { person: "Fred" });
    //~^ ERROR `Struct: Trait<isize>` is not satisfied
    s.f(1);
}


