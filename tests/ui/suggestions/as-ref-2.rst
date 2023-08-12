tests/ui/suggestions/as-ref-2.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Struct;

fn bar(_: &Struct) -> Struct {
    Struct
}

fn main() {
    let foo = Some(Struct);
    let _x: Option<Struct> = foo.map(|s| bar(&s));
    let _y = foo; //~ERROR use of moved value: `foo`
}


