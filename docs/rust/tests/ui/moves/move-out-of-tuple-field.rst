tests/ui/moves/move-out-of-tuple-field.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo(Box<isize>);



fn main() {
    let x: (Box<_>,) = (Box::new(1),);
    let y = x.0;
    let z = x.0; //~ ERROR use of moved value: `x.0`

    let x = Foo(Box::new(1));
    let y = x.0;
    let z = x.0; //~ ERROR use of moved value: `x.0`
}


