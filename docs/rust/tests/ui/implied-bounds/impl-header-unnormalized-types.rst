tests/ui/implied-bounds/impl-header-unnormalized-types.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<T>(T);

trait GoodBye {
    type Forget;
}
impl<T> GoodBye for T {
    type Forget = ();
}

trait NeedsWf<'a, 'b> {
    type Assoc;
}

impl<'a, 'b> NeedsWf<'a, 'b> for Foo<<&'a &'b () as GoodBye>::Forget> {
    type Assoc = &'a &'b ();
    //~^ ERROR in type `&'a &'b ()`, reference has a longer lifetime than the data it references
}

fn needs_wf<'a, 'b, T: NeedsWf<'a, 'b>>() {}

fn foo<'a: 'a, 'b: 'b>(_: &'b String) {
    needs_wf::<'a, 'b, Foo<()>>();
}

fn main() {
    let x = String::from("hello");
    foo::<'static, '_>(&x);
}


