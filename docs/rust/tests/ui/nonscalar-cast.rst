tests/ui/nonscalar-cast.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#[derive(Debug)]
struct Foo {
    x: isize
}

impl From<Foo> for isize {
    fn from(val: Foo) -> isize {
        val.x
    }
}

fn main() {
    println!("{}", Foo { x: 1 } as isize); //~ non-primitive cast: `Foo` as `isize` [E0605]
}


