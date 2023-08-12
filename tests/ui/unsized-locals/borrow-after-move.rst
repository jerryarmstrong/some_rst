tests/ui/unsized-locals/borrow-after-move.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unsized_locals, unsized_fn_params)]
//~^ WARN the feature `unsized_locals` is incomplete

pub trait Foo {
    fn foo(self) -> String;
}

impl Foo for str {
    fn foo(self) -> String {
        self.to_owned()
    }
}

fn drop_unsized<T: ?Sized>(_: T) {}

fn main() {
    {
        let x = "hello".to_owned().into_boxed_str();
        let y = *x;
        drop_unsized(y);
        println!("{}", &x);
        //~^ERROR borrow of moved value
        println!("{}", &y);
        //~^ERROR borrow of moved value
    }

    {
        let x = "hello".to_owned().into_boxed_str();
        let y = *x;
        y.foo();
        println!("{}", &x);
        //~^ERROR borrow of moved value
        println!("{}", &y);
        //~^ERROR borrow of moved value
    }

    {
        let x = "hello".to_owned().into_boxed_str();
        x.foo();
        println!("{}", &x);
        //~^ERROR borrow of moved value
    }
}


