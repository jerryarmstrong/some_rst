tests/ui/methods/assign-to-method.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Zsave-analysis
// Also regression test for #69409

struct Cat {
    meows : usize,
    how_hungry : isize,
}

impl Cat {
    pub fn speak(&self) { self.meows += 1; }
}

fn cat(in_x : usize, in_y : isize) -> Cat {
    Cat {
        meows: in_x,
        how_hungry: in_y
    }
}

fn main() {
    let nyan : Cat = cat(52, 99);
    nyan.speak = || println!("meow"); //~ ERROR attempted to take value of method
    nyan.speak += || println!("meow"); //~ ERROR attempted to take value of method
}


