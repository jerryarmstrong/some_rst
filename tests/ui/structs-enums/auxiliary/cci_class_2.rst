tests/ui/structs-enums/auxiliary/cci_class_2.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub mod kitties {
    pub struct cat {
      meows : usize,

      pub how_hungry : isize,

    }

    impl cat {
        pub fn speak(&self) {}
    }

    pub fn cat(in_x : usize, in_y : isize) -> cat {
        cat {
            meows: in_x,
            how_hungry: in_y
        }
    }
}


