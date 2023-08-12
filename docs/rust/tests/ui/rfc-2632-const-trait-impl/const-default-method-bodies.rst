tests/ui/rfc-2632-const-trait-impl/const-default-method-bodies.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(const_trait_impl)]

#[const_trait]
trait ConstDefaultFn: Sized {
    fn b(self);

    fn a(self) {
        self.b();
    }
}

struct NonConstImpl;
struct ConstImpl;

impl ConstDefaultFn for NonConstImpl {
    fn b(self) {}
}

impl const ConstDefaultFn for ConstImpl {
    fn b(self) {}
}

const fn test() {
    NonConstImpl.a();
    //~^ ERROR the trait bound
    ConstImpl.a();
}

fn main() {}


