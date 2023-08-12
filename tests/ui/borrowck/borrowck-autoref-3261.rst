tests/ui/borrowck/borrowck-autoref-3261.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum Either<T, U> { Left(T), Right(U) }

struct X(Either<(usize,usize), fn()>);

impl X {
    pub fn with<F>(&self, blk: F) where F: FnOnce(&Either<(usize, usize), fn()>) {
        let X(ref e) = *self;
        blk(e)
    }
}

fn main() {
    let mut x = X(Either::Right(main as fn()));
    (&mut x).with(
        |opt| { //~ ERROR cannot borrow `x` as mutable more than once at a time
            match opt {
                &Either::Right(ref f) => {
                    x = X(Either::Left((0, 0)));
                    (*f)()
                },
                _ => panic!()
            }
        })
}


