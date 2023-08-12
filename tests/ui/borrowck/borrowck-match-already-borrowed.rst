tests/ui/borrowck/borrowck-match-already-borrowed.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Foo {
    A(i32),
    B
}

fn match_enum() {
    let mut foo = Foo::B;
    let p = &mut foo;
    let _ = match foo { //~ ERROR [E0503]
        Foo::B => 1,
        _ => 2,
        Foo::A(x) => x //~ ERROR [E0503]
    };
    drop(p);
}


fn main() {
    let mut x = 1;
    let r = &mut x;
    let _ = match x {
        x => x + 1, //~ ERROR [E0503]
        y => y + 2, //~ ERROR [E0503]
    };
    drop(r);
}


