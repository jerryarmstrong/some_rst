tests/ui/no-send-res-ports.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::thread;
use std::rc::Rc;

#[derive(Debug)]
struct Port<T>(Rc<T>);

fn main() {
    #[derive(Debug)]
    struct Foo {
      _x: Port<()>,
    }

    impl Drop for Foo {
        fn drop(&mut self) {}
    }

    fn foo(x: Port<()>) -> Foo {
        Foo {
            _x: x
        }
    }

    let x = foo(Port(Rc::new(())));

    thread::spawn(move|| {
        //~^ ERROR `Rc<()>` cannot be sent between threads safely
        let y = x;
        println!("{:?}", y);
    });
}


