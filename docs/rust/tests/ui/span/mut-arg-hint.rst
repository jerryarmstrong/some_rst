tests/ui/span/mut-arg-hint.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait B {
    fn foo(mut a: &String) {
        a.push_str("bar"); //~ ERROR cannot borrow `*a` as mutable, as it is behind a `&` reference
    }
}

pub fn foo<'a>(mut a: &'a String) {
    a.push_str("foo"); //~ ERROR cannot borrow `*a` as mutable, as it is behind a `&` reference
}

struct A {}

impl A {
    pub fn foo(mut a: &String) {
        a.push_str("foo"); //~ ERROR cannot borrow `*a` as mutable, as it is behind a `&` reference
    }
}

fn main() {
    foo(&"a".to_string());
    A::foo(&"a".to_string());
}


