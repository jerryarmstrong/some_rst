tests/ui/traits/default-method/self.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


trait Cat {
    fn meow(&self) -> bool;
    fn scratch(&self) -> bool { self.purr() }
    fn purr(&self) -> bool { true }
}

impl Cat for isize {
    fn meow(&self) -> bool {
        self.scratch()
    }
}

pub fn main() {
    assert!(5.meow());
}


