tests/ui/rfc-1445-restrict-constants-in-patterns/match-requires-both-partialeq-and-eq.rs
========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Eq)]
struct Foo {
    x: u32
}

impl PartialEq for Foo {
    fn eq(&self, _: &Foo) -> bool {
        false // ha ha!
    }
}

const FOO: Foo = Foo { x: 0 };

fn main() {
    let y = Foo { x: 1 };
    match y {
        FOO => { }
        //~^ ERROR must be annotated with `#[derive(PartialEq, Eq)]`
        _ => { }
    }
}


