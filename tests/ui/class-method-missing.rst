tests/ui/class-method-missing.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait Animal {
  fn eat(&self);
}

struct Cat {
  meows: usize,
}

impl Animal for Cat {
    //~^ ERROR not all trait items implemented, missing: `eat`
}

fn cat(in_x : usize) -> Cat {
    Cat {
        meows: in_x
    }
}

fn main() {
  let nyan = cat(0);
}


