tests/ui/issues/issue-5439.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
    foo: isize,
}

struct Bar {
    bar: isize,
}

impl Bar {
    fn make_foo (&self, i: isize) -> Box<Foo> {
        return Box::new(Foo { nonexistent: self, foo: i }); //~ ERROR: no field named
    }
}

fn main () {
    let bar = Bar { bar: 1 };
    let foo = bar.make_foo(2);
    println!("{}", foo.foo);
}


