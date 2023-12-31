src/tools/miri/tests/pass/issues/issue-3794.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(box_syntax)]

trait T {
    fn print(&self);
}

#[derive(Debug)]
struct S {
    #[allow(dead_code)]
    s: isize,
}

impl T for S {
    fn print(&self) {
        println!("{:?}", self);
    }
}

fn print_t(t: &dyn T) {
    t.print();
}

fn print_s(s: &S) {
    s.print();
}

pub fn main() {
    let s: Box<S> = box S { s: 5 };
    print_s(&*s);
    let t: Box<dyn T> = s as Box<dyn T>;
    print_t(&*t);
}


