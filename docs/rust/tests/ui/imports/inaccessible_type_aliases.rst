tests/ui/imports/inaccessible_type_aliases.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod a {
    type Foo = u64;
    type Bar = u64;
}

mod b {
    type Foo = u64;
}

fn main() {
    let x: Foo = 100; //~ ERROR: cannot find type `Foo` in this scope
    let y: Bar = 100; //~ ERROR: cannot find type `Bar` in this scope
    println!("x: {}, y: {}", x, y);
}


