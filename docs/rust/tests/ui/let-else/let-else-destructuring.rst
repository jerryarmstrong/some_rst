tests/ui/let-else/let-else-destructuring.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Debug)]
enum Foo {
    Done,
    Nested(Option<&'static Foo>),
}

fn walk(mut value: &Foo) {
    loop {
        println!("{:?}", value);
        &Foo::Nested(Some(value)) = value else { break }; //~ ERROR invalid left-hand side of assignment
        //~^ERROR <assignment> ... else { ... } is not allowed
    }
}

fn main() {
    walk(&Foo::Done);
}


