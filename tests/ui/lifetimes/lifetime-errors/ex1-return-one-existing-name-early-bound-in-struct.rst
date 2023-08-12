tests/ui/lifetimes/lifetime-errors/ex1-return-one-existing-name-early-bound-in-struct.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Clone)]
enum Foo<'a> {
    Bar(&'a str),
}

impl<'a> Foo<'a> {
    fn bar(&self, other: Foo) -> Foo<'a> {
        match *self {
            Foo::Bar(s) => {
                if s == "test" {
                    other //~ ERROR explicit lifetime
                } else {
                    self.clone()
                }
            }
        }
    }
}

fn main() { }


