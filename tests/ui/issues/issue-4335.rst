tests/ui/issues/issue-4335.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(fn_traits)]

fn id<T>(t: T) -> T { t }

fn f<'r, T>(v: &'r T) -> Box<dyn FnMut() -> T + 'r> {
    id(Box::new(|| *v))
        //~^ ERROR E0507
}

fn main() {
    let v = &5;
    println!("{}", f(v).call_mut(()));
}


