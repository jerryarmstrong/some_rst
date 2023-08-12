tests/ui/for/for-loop-bogosity.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct MyStruct {
    x: isize,
    y: isize,
}

impl MyStruct {
    fn next(&mut self) -> Option<isize> {
        Some(self.x)
    }
}

pub fn main() {
    let mut bogus = MyStruct {
        x: 1,
        y: 2,
    };
    for x in bogus {
    //~^ ERROR `MyStruct` is not an iterator
        drop(x);
    }
}


