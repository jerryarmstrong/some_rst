tests/ui/moves/moves-based-on-type-block-bad.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_patterns)]


struct S {
    x: Box<E>
}

enum E {
    Foo(Box<S>),
    Bar(Box<isize>),
    Baz
}

fn f<G>(s: &S, g: G) where G: FnOnce(&S) {
    g(s)
}

fn main() {
    let s = S { x: Box::new(E::Bar(Box::new(42))) };
    loop {
        f(&s, |hellothere| {
            match hellothere.x { //~ ERROR cannot move out
                box E::Foo(_) => {}
                box E::Bar(x) => println!("{}", x.to_string()),
                box E::Baz => {}
            }
        })
    }
}


