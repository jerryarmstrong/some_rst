tests/ui/self/class-missing-self.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Cat {
  meows : usize,
}

impl Cat {
    fn sleep(&self) { loop{} }
    fn meow(&self) {
      println!("Meow");
      meows += 1; //~ ERROR cannot find value `meows` in this scope
      sleep();     //~ ERROR cannot find function `sleep` in this
    }

}


 fn main() { }


