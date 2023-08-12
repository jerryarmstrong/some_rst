tests/ui/structs/struct-fields-typo.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct BuildData {
    foo: isize,
    bar: f32
}

fn main() {
    let foo = BuildData {
        foo: 0,
        bar: 0.5,
    };
    let x = foo.baa; //~ ERROR no field `baa` on type `BuildData`
                     //~| HELP a field with a similar name exists
                     //~| SUGGESTION bar
    println!("{}", x);
}


