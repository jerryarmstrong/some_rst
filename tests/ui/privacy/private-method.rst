tests/ui/privacy/private-method.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod kitties {
    pub struct Cat {
        meows : usize,

        how_hungry : isize,
    }

    impl Cat {
        fn nap(&self) {}
    }

    pub fn cat(in_x : usize, in_y : isize) -> Cat {
        Cat {
            meows: in_x,
            how_hungry: in_y
        }
    }
}

fn main() {
  let nyan : kitties::Cat = kitties::cat(52, 99);
  nyan.nap(); //~ ERROR associated function `nap` is private
}


