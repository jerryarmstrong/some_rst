tests/ui/self/move-self.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
struct S {
    x: String
}

impl S {
    pub fn foo(self) {
        self.bar();
    }

    pub fn bar(self) {
        println!("{}", self.x);
    }
}

pub fn main() {
    let x = S { x: "Hello!".to_string() };
    x.foo();
}


