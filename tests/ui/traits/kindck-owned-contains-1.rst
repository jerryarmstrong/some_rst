tests/ui/traits/kindck-owned-contains-1.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(non_snake_case)]
#![allow(non_camel_case_types)]

trait repeat<A> { fn get(&self) -> A; }

impl<A:Clone + 'static> repeat<A> for Box<A> {
    fn get(&self) -> A {
        (**self).clone()
    }
}

fn repeater<A:Clone + 'static>(v: Box<A>) -> Box<dyn repeat<A>+'static> {
    Box::new(v) as Box<dyn repeat<A>+'static> // No
}

pub fn main() {
    let x = 3;
    let y = repeater(Box::new(x));
    assert_eq!(x, y.get());
}


