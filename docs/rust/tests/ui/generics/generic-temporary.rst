tests/ui/generics/generic-temporary.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn mk() -> isize { return 1; }

fn chk(a: isize) { println!("{}", a); assert_eq!(a, 1); }

fn apply<T>(produce: fn() -> T,
            consume: fn(T)) {
    consume(produce());
}

pub fn main() {
    let produce: fn() -> isize = mk;
    let consume: fn(v: isize) = chk;
    apply::<isize>(produce, consume);
}


