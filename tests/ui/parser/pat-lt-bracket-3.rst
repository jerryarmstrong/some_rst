tests/ui/parser/pat-lt-bracket-3.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<T>(T, T);

impl<T> Foo<T> {
    fn foo(&self) {
        match *self {
            Foo<T>(x, y) => {
            //~^ error: expected one of `=>`, `@`, `if`, or `|`, found `<`
              println!("Goodbye, World!")
            }
        }
    }
}

fn main() {}


