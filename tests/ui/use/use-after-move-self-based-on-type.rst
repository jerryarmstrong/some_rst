tests/ui/use/use-after-move-self-based-on-type.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    x: isize,
}

impl Drop for S {
    fn drop(&mut self) {}
}

impl S {
    pub fn foo(self) -> isize {
        self.bar();
        return self.x;  //~ ERROR use of moved value: `self`
    }

    pub fn bar(self) {}
}

fn main() {
    let x = S { x: 1 };
    println!("{}", x.foo());
}


