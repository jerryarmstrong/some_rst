tests/ui/borrowck/borrowck-argument.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[derive(Copy, Clone)]
struct S;

impl S {
    fn mutate(&mut self) {
    }
}

fn func(arg: S) {
    arg.mutate(); //~ ERROR: cannot borrow `arg` as mutable, as it is not declared as mutable
}

impl S {
    fn method(&self, arg: S) {
        arg.mutate(); //~ ERROR: cannot borrow `arg` as mutable, as it is not declared as mutable
    }
}

trait T {
    fn default(&self, arg: S) {
        arg.mutate(); //~ ERROR: cannot borrow `arg` as mutable, as it is not declared as mutable
    }
}

impl T for S {}

fn main() {
    let s = S;
    func(s);
    s.method(s);
    s.default(s);
    (|arg: S| { arg.mutate() })(s);
    //~^ ERROR: cannot borrow `arg` as mutable, as it is not declared as mutable
}


