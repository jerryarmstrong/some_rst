tests/ui/regions/regions-addr-of-self.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Dog {
    cats_chased: usize,
}

impl Dog {
    pub fn chase_cat(&mut self) {
        let p: &'static mut usize = &mut self.cats_chased;
        //~^ ERROR lifetime may not live long enough
        *p += 1;
    }

    pub fn chase_cat_2(&mut self) {
        let p: &mut usize = &mut self.cats_chased;
        *p += 1;
    }
}

fn dog() -> Dog {
    Dog {
        cats_chased: 0
    }
}

fn main() {
    let mut d = dog();
    d.chase_cat();
    println!("cats_chased: {}", d.cats_chased);
}


