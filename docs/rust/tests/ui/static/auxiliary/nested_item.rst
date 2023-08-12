tests/ui/static/auxiliary/nested_item.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // original problem
pub fn foo<T>() -> isize {
    {
        static foo: isize = 2;
        foo
    }
}

// issue 8134
struct Foo;
impl Foo {
    pub fn foo<T>(&self) {
        static X: usize = 1;
    }
}

// issue 8134
pub struct Parser<T>(T);
impl<T: std::iter::Iterator<Item=char>> Parser<T> {
    fn in_doctype(&mut self) {
        static DOCTYPEPattern: [char; 6] = ['O', 'C', 'T', 'Y', 'P', 'E'];
    }
}

struct Bar;
impl Foo {
    pub fn bar<T>(&self) {
        static X: usize = 1;
    }
}


