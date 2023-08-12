tests/ui/generics/generic-exterior-unique.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Recbox<T> {x: Box<T>}

fn reclift<T>(t: T) -> Recbox<T> { return Recbox { x: Box::new(t) }; }

pub fn main() {
    let foo: isize = 17;
    let rbfoo: Recbox<isize> = reclift::<isize>(foo);
    assert_eq!(*rbfoo.x, foo);
}


