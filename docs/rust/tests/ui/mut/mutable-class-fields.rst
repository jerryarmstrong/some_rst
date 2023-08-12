tests/ui/mut/mutable-class-fields.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Cat {
  meows : usize,
  how_hungry : isize,
}

fn cat(in_x : usize, in_y : isize) -> Cat {
    Cat {
        meows: in_x,
        how_hungry: in_y
    }
}

fn main() {
  let nyan : Cat = cat(52, 99);
  nyan.how_hungry = 0; //~ ERROR cannot assign
}


