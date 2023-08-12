tests/ui/borrowck/borrowck-partial-reinit-3.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::mem;

struct Test { f: usize }
impl Drop for Test {
    fn drop(&mut self) {}
}

fn main() {
    let mut x = (Test { f: 2 }, Test { f: 4 });
    mem::drop(x.0);
    x.0.f = 3;
    //~^ ERROR assign of moved value: `x.0`
}


