tests/ui/nll/maybe-initialized-drop-implicit-fragment-drop.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Wrap<'p> { p: &'p mut i32 }

impl<'p> Drop for Wrap<'p> {
    fn drop(&mut self) {
        *self.p += 1;
    }
}

struct Foo<'p> { a: String, b: Wrap<'p> }

fn main() {
    let mut x = 0;
    let wrap = Wrap { p: &mut x };
    let s = String::from("str");
    let foo = Foo { a: s, b: wrap };
    std::mem::drop(foo.b);
    x = 1; //~ ERROR cannot assign to `x` because it is borrowed [E0506]
    // FIXME ^ Should not error in the future with implicit dtors, only manually implemented ones
}


