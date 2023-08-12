tests/ui/new-impl-syntax.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::fmt;

struct Thingy {
    x: isize,
    y: isize
}

impl fmt::Debug for Thingy {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{{ x: {:?}, y: {:?} }}", self.x, self.y)
    }
}

struct PolymorphicThingy<T> {
    x: T
}

impl<T:fmt::Debug> fmt::Debug for PolymorphicThingy<T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self.x)
    }
}

pub fn main() {
    println!("{:?}", Thingy { x: 1, y: 2 });
    println!("{:?}", PolymorphicThingy { x: Thingy { x: 1, y: 2 } });
}


