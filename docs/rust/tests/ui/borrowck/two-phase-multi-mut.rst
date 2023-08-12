tests/ui/borrowck/two-phase-multi-mut.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo {
}

impl Foo {
    fn method(&mut self, foo: &mut Foo) {
    }
}

fn main() {
    let mut foo = Foo { };
    foo.method(&mut foo);
    //~^     cannot borrow `foo` as mutable more than once at a time
    //~^^    cannot borrow `foo` as mutable more than once at a time
}


