tests/ui/walk-struct-literal-with.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Mine{
    test: String,
    other_val: isize
}

impl Mine{
    fn make_string_bar(mut self) -> Mine{
        self.test = "Bar".to_string();
        self
    }
}

fn main(){
    let start = Mine{test:"Foo".to_string(), other_val:0};
    let end = Mine{other_val:1, ..start.make_string_bar()};
    println!("{}", start.test); //~ ERROR borrow of moved value: `start`
}


