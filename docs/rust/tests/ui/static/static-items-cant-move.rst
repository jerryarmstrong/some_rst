tests/ui/static/static-items-cant-move.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Verifies that static items can't be moved

struct B;

struct Foo {
    foo: isize,
    b: B,
}

static BAR: Foo = Foo { foo: 5, b: B };


fn test(f: Foo) {
    let _f = Foo{foo: 4, ..f};
}

fn main() {
    test(BAR); //~ ERROR cannot move out of static item
}


