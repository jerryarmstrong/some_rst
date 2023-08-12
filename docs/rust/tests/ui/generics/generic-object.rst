tests/ui/generics/generic-object.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

trait Foo<T> {
    fn get(&self) -> T;
}

struct S {
    x: isize
}

impl Foo<isize> for S {
    fn get(&self) -> isize {
        self.x
    }
}

pub fn main() {
    let x = Box::new(S { x: 1 });
    let y = x as Box<dyn Foo<isize>>;
    assert_eq!(y.get(), 1);
}


