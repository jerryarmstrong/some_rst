tests/ui/issues/issue-5666.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Dog {
    name : String
}

trait Barks {
    fn bark(&self) -> String;
}

impl Barks for Dog {
    fn bark(&self) -> String {
        return format!("woof! (I'm {})", self.name);
    }
}


pub fn main() {
    let snoopy = Box::new(Dog{name: "snoopy".to_string()});
    let bubbles = Box::new(Dog{name: "bubbles".to_string()});
    let barker = [snoopy as Box<dyn Barks>, bubbles as Box<dyn Barks>];

    for pup in &barker {
        println!("{}", pup.bark());
    }
}


